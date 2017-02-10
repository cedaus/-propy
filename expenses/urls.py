from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^expenses/calendar/$', views.req_expenses_calendar, name='req_expenses_calendar'),
]
