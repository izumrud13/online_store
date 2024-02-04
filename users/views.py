import random

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.html import strip_tags
from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "user/register.html"
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        new_user = form.save(commit=False)
        # Функционал для отправки письма и генерации токена
        token = default_token_generator.make_token(new_user)
        new_user.email_verification_token = token
        new_user.email_verification_token = token
        new_user.save()
        current_site = get_current_site(self.request)

        mail_subject = ('Подтверждение регистрации')
        html_message = render_to_string(
            'users/verification_email.html',
            {
                'user': new_user,
                'domain': current_site.domain,
                'token': token
            })

        plain_message = strip_tags(html_message)
        message = EmailMultiAlternatives(mail_subject,
                                         plain_message,
                                         settings.EMAIL_HOST_USER,
                                         [new_user.email]
                                         )

        message.attach_alternative(html_message, "text/html")
        message.send()
        return response


class VerifyEmailView(View):

    def get(self, request, token):
        try:
            user = User.objects.get(email_verification_token=token)
            user.is_active = True
            user.save()
            return render(request, 'users/registration_success.html')
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Смена пароля',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:index'))
