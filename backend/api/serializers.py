from rest_framework import serializers
from .models import Expense, UserExpense, UserCustom


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class UserExpenseSerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True, required=False)

    class Meta:
        model = UserExpense
        fields = '__all__'


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = '__all__'
