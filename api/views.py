import json

from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(http_method_names=['POST'])
def login(request):
    data = json.loads(str(request.data))
    print(data['username'])
    username = data['username']
    password = data['password']

    print(password)
    return Response(status=200, data={"Hi": "HELOO"})
