from django.shortcuts import render
from django.views import generic

from .forms import PostForm
from .models import Post, Dummy
from .enums import TestEnum


class Landing(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'landing_page.html'
    success_url = '/'


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(Post, self).get_context_data(**kwargs)
    #     context['colors'] = ['red', 'blue']
    #     return context


class Search(generic.ListView):
    model = Dummy
    template_name = 'search.html'
    context_object_name = 'dummies'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['colors'] = ['red', 'blue']
        return context
