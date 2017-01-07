from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import date
from .models import Expense
from .forms import ExpenseForm
# Create your views here

#list of all objects created from class Expense
all_expenses = Expense.objects.all()

#Calculate total expense from an expenses list
def total_expense(expenses_list):
    total_expense = 0
    for expense in expenses_list:
        total_expense += expense.amount
    return total_expense

#Calculating total number of days in an expenses list
def num_days(expenses_list):
    num_days = 0
    for key in daily_expenses(expenses_list):
        num_days += 1
    return num_days

#Calculating average expense in an expenses list
def avg_expense(expense_list):
    avg_expense = total_expense(expense_list) / num_days(expense_list)
    return avg_expense

#Divide expenses based on tags in an expenses list
def diversify_expenses(expenses_list):
    diversify_expenses = {}
    for expense in expenses_list:
        tag = expense.tag
        try:
            diversify_expenses[tag]
        except KeyError:
            diversify_expenses[tag] = 0
        diversify_expenses[tag] += expense.amount
    return diversify_expenses

#Create a list of all expenses by day
def daily_expenses(expenses_list):
    daily_expenses = {}
    for expense in expenses_list:
        date = str(expense.date)
        try:
            daily_expenses[date]
        except KeyError:
            daily_expenses[date] = {'total': 0, 'expenses': []}
        daily_expenses[date]['total'] += expense.amount
        daily_expenses[date]['expenses'].append({'title': expense.title, 'tag': expense.tag, 'amount': expense.amount})
    return daily_expenses

#Calculating total expenses by months
def monthly_expenses():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthly_expenses = []
    num_months = 1

    while (num_months <= 12):
        month_expenses_list = Expense.objects.filter(date__month=num_months)
        if (num_days(month_expenses_list) == 0):
            month_avg = 'NULL'
        else:
            month_avg = avg_expense(month_expenses_list)
        monthly_expenses.append({'month_name': months[num_months - 1], 'month_total': total_expense(month_expenses_list),
         'num_days': num_days(month_expenses_list), 'month_avg': month_avg, 'month_diversify': diversify_expenses(month_expenses_list),
         'month_expenses_list': month_expenses_list, 'month_daily_expenses': daily_expenses(month_expenses_list)})
        num_months += 1

    return monthly_expenses

#Creating form for new expense
def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publish_expenses'))
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_new.html', {'form': ExpenseForm()})

#Publish expenses and related data
def publish_expenses(request):
    return render(request, 'expenses/expenses.html', {'monthly_expenses': monthly_expenses()})
