from django.conf.urls import url

from . import views

app_name = 'event'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<event_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^create/$', views.create2, name='contact'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^(?P<event_id>[0-9]+)/join/$', views.event_join, name='event_join'),
#    url(r'^(?Pevent_id>[0-9]+)/vote/$', views.vote, name='vote'),
]