from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import models, serializers
from mysite.utils import get_value_or_404, get_boolean, get_date_obj, get_month_name
from .utils import get_month_total, get_month_avg, get_month_daily_data, get_month_important, get_month_extra, get_month_tags

class ExpenseReport(APIView):
    def get(self, request, format=None):
        year = int(get_value_or_404(request.GET, 'year'))
        month = int(get_value_or_404(request.GET, 'month'))
        month_name = get_month_name(month)
        month_total = get_month_total(year, month)
        month_avg = get_month_avg(year, month)
        month_important = get_month_important(year, month)
        month_extra = get_month_extra(year, month)
        month_tags = get_month_tags(year, month)
        #Find month daily data
        month_daily_data = get_month_daily_data(year, month)
        for i, item in enumerate(month_daily_data):
            sdata = serializers.ExpenseSerializer(item['expenses'], many=True).data
            month_daily_data[i]['expenses'] = sdata
        #Find a list of total expense of months
        year_monthly_total = []
        for i in range(12):
            year_monthly_total.append(get_month_total(year, i+1))
        #Bundle all the values
        data = {
        'year': year,
        'month': month,
        'month_name': month_name,
        'month_total': month_total,
        'month_avg': month_avg,
        'month_important':  month_important,
        'month_extra': month_extra,
        'month_tags': month_tags,
        'month_daily_data':  month_daily_data,
        'year_monthly_total': year_monthly_total,
        }
        return Response(data, status=status.HTTP_200_OK)


class ExpenseCalendar(APIView):
    def get(self, request, format=None):
        year = int(get_value_or_404(request.GET, 'year'))
        month = int(get_value_or_404(request.GET, 'month'))
        month_total = get_month_total(year, month)
        month_avg = get_month_avg(year, month)
        month_daily_data = get_month_daily_data(year, month)
        for i, item in enumerate(month_daily_data):
            sdata = serializers.ExpenseSerializer(item['expenses'], many=True).data
            month_daily_data[i]['expenses'] = sdata
        data = {'month_total': month_total, 'month_avg': month_avg, 'month_daily_data':  month_daily_data}
        return Response(data, status=status.HTTP_200_OK)


class Expense(APIView):
    def put(self, request, format=None):
        date = get_date_obj(get_value_or_404(request.data, 'date'))
        title = get_value_or_404(request.data, 'title')
        tag_id = get_value_or_404(request.data, 'tag_id')
        tag = get_object_or_404(models.ExpenseTag, id=tag_id)
        comment = get_value_or_404(request.data, 'comment')
        amount = get_value_or_404(request.data, 'amount')
        important = get_boolean(get_value_or_404(request.data, 'important'))
        extra = get_boolean(get_value_or_404(request.data, 'extra'))
        expense_obj = models.Expense.objects.create(date=date, title=title, tag= tag, comment=comment, amount=amount, important=important, extra=extra)
        expense_obj.save()
        sdata = serializers.ExpenseSerializer(expense_obj).data
        return Response(sdata, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        date = get_date_obj(get_value_or_404(request.data, 'date'))
        title = get_value_or_404(request.data, 'title')
        tag_id = get_value_or_404(request.data, 'tag_id')
        tag = get_object_or_404(models.ExpenseTag, id=tag_id)
        comment = get_value_or_404(request.data, 'comment')
        amount = get_value_or_404(request.data, 'amount')
        important = get_boolean(get_value_or_404(request.data, 'important'))
        extra = get_boolean(get_value_or_404(request.data, 'extra'))
        expense_obj = get_object_or_404(models.Expense, pk=pk)
        expense_obj.date = date
        expense_obj.title = title
        expense_obj.tag = tag
        expense_obj.comment = comment
        expense_obj.amount = amount
        expense_obj.important = important
        expense_obj.extra = extra
        expense_obj.save()
        sdata = serializers.ExpenseSerializer(expense_obj).data
        return Response(sdata, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        expense_obj = get_object_or_404(models.Expense, pk=pk)
        sdata = serializers.ExpenseSerializer(expense_obj).data
        expense_obj.delete()
        return Response(sdata, status=status.HTTP_200_OK)
