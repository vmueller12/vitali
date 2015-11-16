"""vitali URL Configuration

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
from django.views.generic.base import TemplateView


from blog import urls as blog_urls
from blog.feed import LatestPosts
from blog.views import BlogDetail

#from messageboard import urls as mess_urls

from django.conf import settings
from django.conf.urls.static import static

from messageboard.views import SentimentDetail, SentimentList, SentimentCreate, SentimentDelete, SentimentUpdate


from contact.views import EmailCreate

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sentiment/(?P<slug>[-\w]+)/delete/$', SentimentDelete.as_view(), name="sent_delete"),
    url(r'^sentiment/(?P<slug>[-\w]+)/update/$', SentimentUpdate.as_view(), name="sent_update"),
    url(r'^sentiment/create/$', SentimentCreate.as_view(), name="sent_create"),
    url(r'^sentiment/(?P<slug>[-\w]+)/$', SentimentDetail.as_view(), name="sent_detail"),
    url(r'^sentiment/$', SentimentList.as_view(), name="sent_list"),
    #Email or Contact URL
    url(r'^contact/$', EmailCreate.as_view(), name="email_create"),
    url(r'^contact/thanks/$', TemplateView.as_view(template_name='contact/thanks.html'), name="contact_thanks"),
    
    #url(r'^feed/$', LatestPosts(), name='feed'),
    #url(r'^(?P<slug>\S+)$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^blog/$', include(blog_urls)),
    #url(r'^messages/$', include(mess_urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^$', TemplateView.as_view(template_name = 'vitali/index.html'), name='home'),
]