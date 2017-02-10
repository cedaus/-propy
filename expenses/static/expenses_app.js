function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showMonthExpCal(month_id) {
  $.ajax({
    type: "POST",
    url: show_month_expenses_url,
    data: {month_id: month_id},
    dataType: "html",
    success: function(response) {
      console.log(response);
      $("#month-expense-calendar").find(".section-body").html(response);
    },
    error: function(request, errorType, errorMessage) {
      alert("Error: " + errorType + " with message: " + errorMessage);
    },
    timeout: 3000,
    beforeSend: function(xhr) { xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); },
    complete: function() {},
    cache: true
  });
}
