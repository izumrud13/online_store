from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from catalog.apps import MainConfig
from catalog.views import IndexView, contacts, mailing, CategoryListView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('mailing/', mailing, name='mailing'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
    path('product/create/',  never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/update/<int:pk>/',  never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/delete/<int:pk>/',  never_cache(ProductDeleteView.as_view()), name='product_delete'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_view')
]
