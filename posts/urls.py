from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home, name='posts_home'),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^update/(?P<id>\d+)/$', views.post_update, name='post_update'),
    url(r'^delete/(?P<id>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^create/$', views.post_create, name='post_create'),
]
