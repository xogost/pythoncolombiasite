from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.groups, name='groups'),
    url(r'groups/$', views.groups, name='groups'),
    url(r'members/(\d+)/$', views.members, name='members'),
    url(r'events/$', views.events, name='events')
]