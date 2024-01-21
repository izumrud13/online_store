from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete')
]
