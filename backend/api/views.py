from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Expense, UserCustom
from .serializers import ExpenseSerializer, UserCustomSerializer,\
    CreateUserSerializer


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CreateExpense(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = (IsAuthenticated, )
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class UserCustomDetail(generics.RetrieveDestroyAPIView):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer


class CreateUserCustom(generics.CreateAPIView):
    serializer_class = UserCustomSerializer


class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        token = Token.objects.create(user=serializer.instance)
        token_data = {'token': token.key}
        return response.Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class LogoutUser(views.APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # just remove the token to force a login
        request.user.auth_token.delete()
