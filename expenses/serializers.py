import models
from rest_framework import serializers


class ExpenseTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExpenseTag
        fields = ['id', 'name', 'icon']

class ExpenseSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField('get_tag_')

    def get_tag_(self, obj):
        tag_obj = ExpenseTagSerializer(obj.tag).data
        return tag_obj

    class Meta:
        model = models.Expense
        fields = ['pk', 'date', 'title', 'tag', 'comment', 'amount', 'important', 'extra']
