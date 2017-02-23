from __future__ import unicode_literals
from django.db import models
from datetime import date

class ExpenseTag(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=75, unique=True)
    icon = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

class Expense(models.Model):
    date = models.DateField(default=date.today)
    title = models.CharField(max_length = 50, default='title')
    tag = models.ForeignKey(ExpenseTag, null=True, default=12, blank=True)
    extra = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.TextField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date) + "   " + self.title
