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
        print(kind)
        try:
            user = user_models.User.objects.get(username=phone)
            price = 0
            if(kind == "Bird"):
                kind = pet_models.Pet.BIRD
                price = 5
            elif(kind == "Cat"):
                kind = pet_models.Pet.CAT
                price = 20
            elif(kind == "Chicken"):
                kind = pet_models.Pet.CHICKEN
                price = 10
            elif(kind == "Cow"):
                kind = pet_models.Pet.COW
                price = 30
            elif(kind == "Dog"):
                kind = pet_models.Pet.DOG
                price = 25
            elif(kind == "Duck"):
                kind = pet_models.Pet.DUCK
                price = 8
            elif(kind == "Elephant"):
                kind = pet_models.Pet.ELEPHANT
                price = 35
            elif(kind == "Koala"):
                kind = pet_models.Pet.KOALA
                price = 15
            elif(kind == "Llama"):
                kind = pet_models.Pet.LLAMA
                price = 18
            elif(kind == "Penguin"):
                kind = pet_models.Pet.PENGUIN
                price = 27
            strawberry = user.strawberry
            if(strawberry < price):
                print("here")
                return HttpResponse("PriceError")
            else:
                user.strawberry = strawberry-price
                user.save()
                pet = pet_models.Pet.objects.create(user=user, kind=kind)
                pet.save()
                return HttpResponse("PetCreate")
        except:
            return HttpResponse("UserNotExist")
