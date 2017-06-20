import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework.authentication import *
from rest_framework.authtoken.models import Token
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
