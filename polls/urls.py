from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^polls/$', views.index, name='index'),
    url(r'^polls/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^polls/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
