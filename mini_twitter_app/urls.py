from django.conf.urls import url, include
from django.urls import path

from mini_twitter_app import views


urlpatterns = [
    url(r'^$', views.explore, name='explore'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^tweet/$', views.tweet, name='tweet'),
]
