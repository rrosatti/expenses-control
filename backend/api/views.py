from rest_framework import generics
from .models import Expense, UserExpense, UserCustom
from .serializers import ExpenseSerializer, UserExpenseSerializer,\
    UserCustomSerializer


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CreateExpense(generics.CreateAPIView):
    serializer_class = ExpenseSerializer


class UserCustomDetail(generics.RetrieveDestroyAPIView):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer


class CreateUserCustom(generics.CreateAPIView):
    serializer_class = UserCustomSerializer


class UserExpenseList(generics.ListCreateAPIView):
    queryset = UserExpense.objects.all()
    serializer_class = UserExpenseSerializer


class UserExpenseDetail(generics.RetrieveDestroyAPIView):
    queryset = UserExpense.objects.all()
    serializer_class = UserExpenseSerializer
