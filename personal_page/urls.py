from django.conf.urls import patterns, url

from personal_page import views

urlpatterns = patterns('',
	url(r'^login/$', views.login, name='login'),
	url(r'^create/$', views.create, name='create'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^edit/post(?P<id>\d+)/$', views.edit, name='edit'),
	url(r'^update/post(?P<id>\d+)/$', views.update, name='update'),
	url(r'^delete/post(?P<id>\d+)/$', views.delete, name='delete'),
	url(r'^logout/$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
)