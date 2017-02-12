import calendar
from mysite.utils import get_date_str, get_current_year, get_current_month, get_current_day, get_month_total_days, get_dict_index_from_list
from .models import ExpenseTag, Expense
from .serializers import ExpenseTagSerializer

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

def get_month_tags(year, month):
    tags = ExpenseTagSerializer(ExpenseTag.objects.all(), many=True).data
    for tag in tags:
        tag['total'] = 0
    expenses = get_month_expenses(year, month)
    for expense in expenses:
        tag_id = expense.tag.id
        amount = expense.amount
        index = get_dict_index_from_list(tags, 'id', tag_id)
        tags[index]['total'] += amount
    return tags

def get_month_important(year, month):
    total = 0
    expenses = Expense.objects.filter(date__year=year, date__month=month, important=True).order_by('date')
    for expense in expenses:
        total += expense.amount
    return total

def get_month_extra(year, month):
    total = 0
    expenses = Expense.objects.filter(date__year=year, date__month=month, extra=True).order_by('date')
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

    daily_data = [{'date': None, 'total' : 0, 'expenses': []} for i in range(month_total_days)]
    for expense in expenses:
        day = int(expense.date.strftime("%d"))
        daily_data[day - 1]['date'] = get_date_str(year, month, day)
        daily_data[day - 1]['total'] += expense.amount
        daily_data[day - 1]['expenses'].append(expense)
    return daily_data
