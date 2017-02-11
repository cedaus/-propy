import calendar
from mysite.utils import get_date_str, get_current_year, get_current_month, get_current_day, get_month_total_days
from .models import ExpenseTag, Expense

def all_tags_total_amount(expenses):
    list_ = []
    for expense in expenses:
        tag = expense.tag
        try:
            diversify_expenses[tag]
        except KeyError:
            diversify_expenses[tag] = 0
        diversify_expenses[tag] += expense.amount
    return diversify_expenses

def get_month_expenses(year, month):
    expenses = Expense.objects.filter(date__year=year, date__month=month).order_by('date')
    return expenses

def get_month_total(year, month):
    total = 0
    expenses = get_month_expenses(year, month)
    for expense in expenses:
        total += expense.amount
    return total

def get_month_avg(year, month):
    curr_year = get_current_year()
    curr_month = get_current_month()
    curr_day = get_current_day()
    month_total_days = get_month_total_days(year, month)
    expenses = get_month_expenses(year, month)
    month_total = get_month_total(year, month)
    if (year == curr_year and month == curr_month):
        avg = month_total / curr_day
    else:
        avg = month_total / month_total_days
    return avg

#Generating expenses data for a month
def get_month_daily_data(year, month):
    month_total_days = get_month_total_days(year, month)
    expenses = get_month_expenses(year, month)

    daily_data = [{'day_date': None, 'day_total' : 0, 'day_expenses': []} for i in range(month_total_days)]
    for expense in expenses:
        day = int(expense.date.strftime("%d"))
        daily_data[day - 1]['day_date'] = get_date_str(year, month, day)
        daily_data[day - 1]['day_total'] += expense.amount
        daily_data[day - 1]['day_expenses'].append(expense)
    return daily_data
