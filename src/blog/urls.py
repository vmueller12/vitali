from django.conf.urls import url
from .views import BlogIndex, BlogDetail
from .feed import LatestPosts


urlpatterns = [
    url(r'^$', BlogIndex.as_view(), name='blog_list'),
    #url(r'feed/$', LatestPosts(), name='feed'),
    #url(r'(?P<slug>\S+)$', BlogDetail.as_view(), name='blog_detail'),
]