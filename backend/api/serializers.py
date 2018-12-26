from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Expense, UserCustom
from django.contrib.auth import get_user_model


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('value', 'date', 'short_desc', 'long_desc')

    def create(self, user, validated_data):
        return Expense.objects.create(
            user=user,
            value=validated_data['value'],
            date=validated_data['date'],
            short_desc=validated_data['short_desc'],
            long_desc=validated_data['long_desc']
        )


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('max_value', 'send_notifications')

    def create(self, user, validated_data):
        return UserCustom.objects.create(
            user=user,
            max_value=validated_data['max_value'],
            send_notifications=validated_data['send_notifications']
        )


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
