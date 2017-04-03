from django.contrib import messages
from django.shortcuts import resolve_url
from django.views.generic import TemplateView, CreateView

from blogs.models import Blog, Post, Like
from comments.models import Comment
from core.forms import UserCreationForm
from core.models import User


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        messages.info(self.request, '<div style="red">Another message<div>')
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['n_users'] = User.objects.all().count()
        context['n_blogs'] = Blog.objects.all().count()
        context['n_posts'] = Post.objects.all().count()
        context['n_comments'] = Comment.objects.all().count()
        context['n_likes'] = Like.objects.all().count()
        return context


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'core/register.html'

    def get_success_url(self):
        return resolve_url('core:login')

    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)