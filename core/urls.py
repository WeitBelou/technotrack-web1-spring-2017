from django.conf.urls import url
from django.contrib.auth.views import logout, login

from core.views import RegisterView

urlpatterns = [
    url(r'^login/', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
]
