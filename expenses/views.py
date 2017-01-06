from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import date
from .models import Expense
from .forms import ExpenseForm
# Create your views here

#list of all objects created from class Expense
all_expenses = Expense.objects.all()

#Create a list of all expenses by dates
def daily_expenses_list():
    daily_expenses = {}
    for expense in all_expenses:
        date = str(expense.date)
        try:
            daily_expenses[date]
        except KeyError:
            daily_expenses[date] = []
        daily_expenses[date].append({'title': expense.title, 'tag': expense.tag, 'amount': expense.amount})
    return daily_expenses

#Divide expenses based on tags
def diversify_expenses():
    diversify_expenses = {}
    for expense in all_expenses:
        tag = str(expense.tag)
        try:
            diversify_expenses[tag]
        except KeyError:
            diversify_expenses[tag] = 0
        diversify_expenses[tag] += expense.amount
    return diversify_expenses

#Create a list of total expenses by dates
def daily_total_list():
    daily_total = {}
    for key in daily_expenses_list():
        daily_total[key] = 0
        for expense in daily_expenses_list()[key]:
            daily_total[key] += expense['amount']
    return daily_total

#Calculate total expenses of month
def total_expense():
    total_expense = 0
    for expense in all_expenses:
        total_expense += expense.amount
    return total_expense

#Calculating total number of days
def num_days():
    num_days = 0
    for key in daily_expenses_list():
        num_days += 1
    return num_days

def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            """date = request.POST.get('date', '')
            title = request.POST.get('title', '')
            tag = request.POST.get('tag', '')
            comment = request.POST.get('comment', '')
            amount = request.POST.get('amount', '')
            expense_new = Expense(date = date, title = title, tag = tag, comment = comment, amount = amount)
            expense_new.save()"""
            return HttpResponseRedirect(reverse('expenses:expense_new'))
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_new.html', {'form': ExpenseForm()})

#Publish expenses and related data
def publish_expenses(request):
    avg_expense = total_expense() / num_days()
    return render(request, 'expenses/expenses.html', {
    'expenses': daily_expenses_list(),
    'total_expense': total_expense(),
    'avg_expense': avg_expense,
    'daily_total': daily_total_list(),
    'diversify_expenses': diversify_expenses(),
    })
