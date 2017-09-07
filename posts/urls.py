from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home, name='posts_home'),
    url(r'^detail/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^update/(?P<slug>[\w-]+)/$', views.post_update, name='post_update'),
    url(r'^delete/(?P<slug>[\w-]+)/$', views.post_delete, name='post_delete'),
    url(r'^create/$', views.post_create, name='post_create'),
]
