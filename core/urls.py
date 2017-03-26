from django.conf.urls import url
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^login/', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name='logout'),
]
