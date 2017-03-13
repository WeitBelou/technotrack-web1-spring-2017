from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from core.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)