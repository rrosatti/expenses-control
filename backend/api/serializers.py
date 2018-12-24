from rest_framework import serializers
from .models import Expense, UserExpense, UserCustom
from django.contrib.auth import get_user_model


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


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name')
        write_only_fields = ('is_staff', 'is_superuser', 'is_active',)

        def create(self, validated_data):
            user = super(CreateUserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user
