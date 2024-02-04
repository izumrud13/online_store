from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


# Create your views here.

class IndexView(TemplateView):
    template_name = 'catalog/index.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}):\n{message}')
    return render(request, 'catalog/contacts.html')


def mailing(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
    return render(request, 'catalog/mailing.html')


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset




class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('catalog:category')

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)




class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object



