from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth import views
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login
#from django.contrib.auth.views import logout

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#	url(r'^login/$',  'django.contrib.auth.views.login', name='login'),
#    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
#    url(r'^login/$', views.login, name='login'),
#    url(r'^logout/$', views.logout, name='logout'),
#    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
#    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
#    url(r'^password_reset/$', views.password_reset, name='password_reset'),
#    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
#    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$views.password_reset_confirm, name='password_reset_confirm'),
#    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]
