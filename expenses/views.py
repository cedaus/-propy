from django.shortcuts import render
from .models import ExpenseTag
from mysite.utils import get_current_year, get_current_month
from .utils import get_month_total, get_month_avg, get_month_daily_data

#Request Expenses Calendar
def req_expenses_calendar(request):
    all_tags = ExpenseTag.objects.all()
    data = {'all_tags': all_tags}
    return render(request, 'expenses/calendar.html', data)
