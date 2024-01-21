from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Category, Product


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

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #
    #     product_item = Product.object.get(pk=self.kwargs.get("pk"))
    #     context_data['product_pk'] = product_item.pk
    #
    #
    #     return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'category', 'description', 'img', 'cost',)
    success_url = reverse_lazy('catalog:category')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'category', 'description', 'img', 'cost',)
    success_url = reverse_lazy('catalog:category')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')



