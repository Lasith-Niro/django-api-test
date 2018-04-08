from django.conf.urls import url

from . import views

urlpatterns = [
    url('stories/', views.home, name='home'),
    url(r'^story/(?P<story_id>\w{1,5})$', views.getOne, name='getOne'),
    url(r'^story/(?P<story_id>\w{1,5})/rating$', views.getRatings, name='getRatings'),
    url(r'^story/(?P<story_id>\w{1,5})/update/(?P<rate>\w{1,5})$', views.updateRatings, name='updateRatings'),
    url(r'^story/update', views.updateTest, name='updateTest'),    

]