from django.conf.urls import url, include

urlpatterns = [
    url(r'^expenses/', include('expenses.api_urls')),
]
