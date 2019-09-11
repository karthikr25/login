from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.Loginview, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.Logoutview, {'template_name': 'logged_out.html'}, name='logout'),
]
