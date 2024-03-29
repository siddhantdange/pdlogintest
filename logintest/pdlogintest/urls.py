
from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^submitprofile/$', views.submitprofile, name='submitprofile'),
    url(r'^(?P<user_name>\S+)/$', views.userpage, name='userpage')
)
