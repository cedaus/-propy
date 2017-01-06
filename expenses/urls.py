from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^expenses/$', views.publish_expenses, name='publish_expenses'),
    url(r'^expenses/new/$', views.expense_new, name='expense_new'),
]
