from django.conf.urls import url

from blogs.views import BlogList, BlogDetails, PostDetails, CreateBlog, UpdateBlog, CreatePost, UpdatePost, \
    PostLikeAjax, DeleteBlog, DeletePost

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^create_blog/', CreateBlog.as_view(), name='create_blog'),
    url(r'^update_blog/(?P<pk>\d+)$', UpdateBlog.as_view(), name='update_blog'),
    url(r'^delete_blog/(?P<pk>\d+)$', DeleteBlog.as_view(), name='delete_blog'),

    url(r'^(?P<pk>\d+)$', BlogDetails.as_view(), name='blog_details'),

    url(r'^posts/(?P<pk>\d+)$', PostDetails.as_view(), name='post_details'),
    url(r'^create_post/', CreatePost.as_view(), name='create_post'),
    url(r'^update_post/(?P<pk>\d+)', UpdatePost.as_view(), name='update_post'),
    url(r'^delete_post/(?P<pk>\d+)', DeletePost.as_view(), name='delete_post'),

    url(r'^posts/likes/(?P<pk>\d+)', PostLikeAjax.as_view(), name='like_post')
]
