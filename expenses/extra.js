
//expenses_list for all months
$(document).ready(function() {
  var expenses_list_check = '{{expenses_list}}';
  if(expenses_list_check) {
    {% for month in expenses_list %}
    var month_obj = new Object();

    month_obj.month_id = '{{month.month_id}}';
    month_obj.month_name = '{{month.month_name}}';
    month_obj.total_days = '{{month.total_days}}';
    {% if month.month_total %} month_obj.month_total = '{{month.month_total}}'; {% endif %}
    {% if month.month_avg %} month_obj.month_avg = '{{month.month_avg}}'; {% endif %}

    {% if month.month_daily_expenses %}
      var month_daily_expenses = []

      {% for day in month.month_daily_expenses %}
      var day_obj = new Object();

      day_obj.total = '{{day.total}}';

      month_daily_expenses.push(day_obj);
      {% endfor %}

      month_obj.month_daily_expenses = month_daily_expenses;
    {% endif %}

    expenses_list.push(month_obj);
    {% endfor %}
  }
});
