# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from . import models as user_models
import json
from django.http import HttpResponse
import base64

@csrf_exempt
@api_view(["POST", "GET"])
def login(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        pwd = request.GET.get("pwd")
        phone = base64.b64decode(phone)
        phone = str(phone, "UTF-8")
        pwd = base64.b64decode(pwd)
        pwd = str(pwd, "UTF-8")
        try:
            user = user_models.User.objects.get(username=phone)
            if(user.pwd != pwd):
                return HttpResponse("PasswordError")
            else:
                return HttpResponse("LoginSuccess")
        except:
            return HttpResponse("IdError")

@csrf_exempt
@api_view(["POST", "GET"])
def create(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        pwd = request.GET.get("pwd")
        phone = base64.b64decode(phone)
        phone = str(phone, "UTF-8")
        pwd = base64.b64decode(pwd)
        pwd = str(pwd, "UTF-8")
        try:
            user = user_models.User.objects.get(username=phone)
            return HttpResponse("AlreadyExist")
        except:
            user = user_models.User.objects.create(username=phone, pwd=pwd)
            user.save()
            return HttpResponse("Create")