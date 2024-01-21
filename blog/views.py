from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Все отзывы'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_publications=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'sign_publications',)
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'Написать отзыв'
    }


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'sign_publications',)
    success_url = reverse_lazy('blog:blog')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogDeleteView(DeleteView):
    model = Blog
    permission_required = 'catalog.delete_review'
    success_url = reverse_lazy('catalog:reviews')




