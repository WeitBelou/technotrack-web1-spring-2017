from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from core.views import HomePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
]

if settings.SERVE_MEDIA_FILES:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
