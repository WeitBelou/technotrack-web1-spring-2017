from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView

from core.views import HomePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    url(r'^comments/', include('comments.urls', namespace='comments')),

    url(r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('core/images/favicon.ico'),
            permanent=False),
        name='favicon'
        )
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        url(r'__debug__/', include(debug_toolbar.urls)),
    )
