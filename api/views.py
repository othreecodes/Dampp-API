import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework.authentication import *
from rest_framework.authtoken.models import Token

from api.models import User
from .serializers import UserSerializer


# Create your views here.

@api_view(http_method_names=['POST'])
def login_user(request):
    data = json.loads(str(request.data))
    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        token = Token.objects.get_or_create(user=user)

        login(request, user)
        user = UserSerializer(user)

        data = {
            'message': 'Valid User',
            'token': str(token[0]),
            'user': user.data,
            'code': 100,
        }

    else:
        data = {
            'message': 'Invalid Details',
            'code': 101
        }
    return Response(status=200, data=data)


class Suggestions(APIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass


class Matches(APIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass


class UserView(APIView):
    def post(self, request):
        print(request.data)

        data = json.loads(str(request.data))
        username = data['username']
        full_name = data['full_name']
        sex = data['sex']
        password = data['password']

        print(User.objects.filter(username=username).first())
        if User.objects.filter(username=username).first() is not None:
            context = {
                "error": 102,
                "message": "Username already taken"
            }
            return JsonResponse(data=context, status=200)

        return JsonResponse(status=200, data="OK")
