import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework.authentication import *
from rest_framework.authtoken.models import Token

from api.models import User, Profile
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
    def posst(self, request):
        context = {"code": 100, "token": "05b0e6bc00d03037cea7b0084a5d3aca8fb36a1e",
                   "message": "Registration successful", "user": {"id": 5,
                                                                  "password": "pbkdf2_sha256$36000$XoreUgIUj1kc$tXMTUxaKuP05xB+xL9JHdFrZOFRA1RjTKZMkUszAwA4=",
                                                                  "last_login": None, "is_superuser": False,
                                                                  "username": "lala", "first_name": "", "last_name": "",
                                                                  "email": "", "is_staff": False, "is_active": True,
                                                                  "date_joined": "2017-06-26T13:57:09.999178Z",
                                                                  "is_verified": False, "photo_url": "",
                                                                  "full_name": "Akinkuolie Precious", "sex": "Female",
                                                                  "groups": [], "user_permissions": []}}
        return JsonResponse(data=context,status=200)

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

        user = User.objects.create(username=username, full_name=full_name, sex=sex)
        user.set_password(password)
        user.save()

        profile = Profile.objects.create(user=user)
        profile.save()
        token = Token.objects.get_or_create(user=user)

        context = {
            "code": 100,
            "message": "Registration successful",
            "user": UserSerializer(user).data,
            "token": str(token[0])
        }

        return JsonResponse(status=200, data=context)
