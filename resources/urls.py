from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resources/(?P<category_id>[0-9]+)/resources-list/$', views.req_category_resources_list, name='req_category_resources_list'),
    url(r'^resources/(?P<category_id>[0-9]+)/collections/$', views.req_category_collections, name='req_category_collections'),
]
