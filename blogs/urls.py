from django.conf.urls import url

from blogs.views import BlogList, BlogDetails

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)$', BlogDetails.as_view(), name='blog_details'),
]