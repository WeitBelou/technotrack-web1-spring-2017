from django.conf.urls import url

from blogs.views import BlogList

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list')
]