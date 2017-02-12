from django.conf.urls import url, include
import rest_views

urlpatterns = [
    url(r'^expense/report/$', rest_views.ExpenseReport.as_view(), name='expense_report'),
    url(r'^expense/calendar/$', rest_views.ExpenseCalendar.as_view(), name='expense_calendar'),
    url(r'^expense/new/$', rest_views.Expense.as_view(), name='expense_new'),
    url(r'^expense/(?P<pk>[-\w\d]+)/$', rest_views.Expense.as_view(), name='expense_data'),
]
