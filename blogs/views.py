from django.shortcuts import render
from django.views.generic import ListView

from blogs.models import Blog


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog