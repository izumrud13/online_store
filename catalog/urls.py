from django.urls import path

from catalog.apps import MainConfig
from catalog.views import IndexView, contacts, mailing, CategoryListView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('mailing/', mailing, name='mailing'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')

]