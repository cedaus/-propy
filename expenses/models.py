from django.db import models
from datetime import date
# Create your models here.

class Expense(models.Model):
    date = models.DateField(default=date.today)
    title = models.CharField(max_length = 50, default='title')
    tag = models.CharField(max_length = 25)
    comment = models.TextField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date) + "   " + self.title
