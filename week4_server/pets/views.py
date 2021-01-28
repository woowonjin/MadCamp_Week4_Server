# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from . import models as pet_models
from users import models as user_models
import json
from django.http import HttpResponse
import base64

@csrf_exempt
@api_view(["POST", "GET"])
def get_pets(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        phone = base64.b64decode(phone)
        phone = str(phone, "UTF-8")
        print(phone)
        try:
            user = user_models.User.objects.get(username=phone)
            pets = pet_models.Pet.objects.filter(user=user)
            pets_kind = []
            for pet in pets:
                pets_kind.append(pet.serialize_custom())
            pets_json = json.dumps(pets_kind)
            return HttpResponse(pets_json, content_type="text/json-comment-filtered")
        except:
            return HttpResponse("UserNotExist")

@csrf_exempt
@api_view(["POST", "GET"])
def create(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        kind = request.GET.get("kind")
        phone = base64.b64decode(phone)
        phone = str(phone, "UTF-8")
        kind = base64.b64decode(kind)
        kind = str(kind, "UTF-8")
        print(phone)
        try:
            user = user_models.User.objects.get(username=phone)
            if(kind == "Bird"):
                kind = pet_models.Pet.BIRD
            elif(kind == "Cat"):
                kind = pet_models.Pet.CAT
            elif(kind == "Chicken"):
                kind = pet_models.Pet.CHICKEN
            elif(kind == "Cow"):
                kind = pet_models.Pet.COW
            elif(kind == "Dog"):
                kind = pet_models.Pet.DOG
            elif(kind == "Duck"):
                kind = pet_models.Pet.DUCK
            elif(kind == "Elephant"):
                kind = pet_models.Pet.ELEPHANT
            elif(kind == "Koala"):
                kind = pet_models.Pet.KOALA
            elif(kind == "Llama"):
                kind = pet_models.Pet.LLAMA
            elif(kind == "Penguin"):
                kind = pet_models.Pet.PENGUIN

            pet = pet_models.Pet.objects.create(user=user, kind=kind)
            pet.save()
            return HttpResponse("PetCreate")
        except:
            return HttpResponse("UserNotExist")