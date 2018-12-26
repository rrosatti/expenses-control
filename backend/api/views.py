from django.contrib.auth import get_user_model
from rest_framework import generics, status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Expense, UserCustom
from .serializers import ExpenseSerializer, UserCustomSerializer,\
    CreateUserSerializer


class ExpenseViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = (IsAuthenticated, )
    serializer_class = ExpenseSerializer

    def list(self, request):
        queryset = Expense.objects.filter(user=request.user)
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, expense_id=None):
        queryset = Expense.objects.all()
        expense = get_object_or_404(queryset, pk=expense_id)
        serializer = ExpenseSerializer(expense)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create(
                user=request.user,
                validated_data=serializer.validated_data)

            return Response(
                serializer.validated_data,
                status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserCustomViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = (IsAuthenticated, )
    serializer_class = UserCustomSerializer

    def retrieve(self, request, pk=None):
        queryset = UserCustom.objects.all()
        user_custom = get_object_or_404(queryset, user=request.user)
        serializer = UserCustomSerializer(user_custom)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserCustomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create(
                user=request.user,
                validated_data=serializer.validated_data)

            return Response(
                serializer.validated_data,
                status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        token = Token.objects.create(user=serializer.instance)
        token_data = {'token': token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class LogoutUser(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # just remove the token to force a login
        request.user.auth_token.delete()
