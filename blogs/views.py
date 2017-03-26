from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import resolve_url
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView

from blogs.models import Blog, Post


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'description', 'category')

    template_name = 'blogs/create_blog.html'

    def get_success_url(self):
        return resolve_url('blogs:blog_details', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBlog, self).form_valid(form)


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'description', 'category')

    template_name = 'blogs/update_blog.html'

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return resolve_url('blogs:blog_details', pk=self.object.pk)


class BlogDetails(DetailView):
    template_name = 'blogs/blog_details.html'
    model = Blog


class PostDetails(DetailView):
    template_name = 'blogs/post_details.html'
    model = Post


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('blog', 'title', 'content',)

    template_name = 'blogs/create_post.html'

    def get_success_url(self):
        return resolve_url('blogs:post_details', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'content',)

    template_name = 'blogs/update_post.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('blogs:post_details', pk=self.object.pk)
