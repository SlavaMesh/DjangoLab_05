from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.db import models
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class NewsList(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-date'
    template_name = '../templates/flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class SearchList(ListView):
    model = Post
    ordering = '-date'
    template_name = '../templates/flatpages/search.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = '../templates/flatpages/post.html'
    context_object_name = 'post'


class ADD(PermissionRequiredMixin, CreateView):
    template_name = '../templates/flatpages/add.html'
    form_class = PostForm
    permission_required = ('news.add_post')

class Update(PermissionRequiredMixin, UpdateView):
    template_name = '../templates/flatpages/add.html'
    form_class = PostForm
    permission_required = ('news.change_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class Delete(PermissionRequiredMixin, DeleteView):
    template_name = '../templates/flatpages/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post')