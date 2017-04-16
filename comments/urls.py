from django.conf.urls import url

from comments.views import CommentsList

urlpatterns = [
    url('^(?P<post>\d+)$', CommentsList.as_view(), name='comments')
]