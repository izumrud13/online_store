from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from catalog.models import Category


# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


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

def category(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request, 'catalog/category.html', context)


