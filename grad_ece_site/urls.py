"""grad_ece_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from grad_forms import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^ms_pos_form/', views.ms_pos_form, name="ms_pos_form"),
    url(r'^phd_pos_form/', views.phd_pos_form, name="phd_pos_form"),
    url(r'^meng_pos_form/', views.meng_pos_form, name='meng_pos_form'),
    url(r'^independent_study_form/', views.independent_study_form, name='independent_study_form'),
    url(r'^admin/', include(admin.site.urls)),
]
