# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from . import models as quest_models
from users import models as user_models
import json
from django.http import HttpResponse, JsonResponse
import base64


# Ho, Hae, Chan, Kang, Yoon

@csrf_exempt
@api_view(["POST", "GET"])
def get_quest(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        phone = base64.b64decode(phone)
        phone = str(phone, "UTF-8")
        npc = request.GET.get("npc")
        npc = base64.b64decode(npc)
        npc = str(npc, "UTF-8")
        try:
            print(phone)
            print(npc)
            user = user_models.User.objects.get(username=phone)
            if(npc == "Ho"):
                npc = quest_models.Quest.HOBIN
            elif(npc == "Hae"):
                npc = quest_models.Quest.HAECHEOL
            elif(npc == "Chan"):
                npc = quest_models.Quest.CHANI
            elif(npc == "Kang"):
                npc = quest_models.Quest.KANGWOOK
            elif(npc == "Yoon"):
                npc = quest_models.Quest.YOON
            quest = quest_models.Quest.objects.filter(user=user).get(npc=npc)
            print(quest.is_solved)
            if(quest.is_solved):
                print("quest is solved")
                return HttpResponse("AlreadySolved")
            else:
                response = {
                    "question" : quest.problem.question,
                    "answer" : quest.problem.answer,
                    "reward" : quest.problem.reward,
                    "npc" : quest.npc,
                }
                return JsonResponse(response,json_dumps_params={'ensure_ascii': False}, status=200)
        except:
            return HttpResponse("UserNotExist")

@csrf_exempt
@api_view(["POST", "GET"])
def clear_quest(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        phone = base64.b64decode(phone)
        phone = str(phone, "UTF-8")
        npc = request.GET.get("npc")
        npc = base64.b64decode(npc)
        npc = str(npc, "UTF-8")
        try:
            user = user_models.User.objects.get(username=phone)
            if(npc == "Ho"):
                npc = quest_models.Quest.HOBIN
            elif(npc == "Hae"):
                npc = quest_models.Quest.HAECHEOL
            elif(npc == "Chan"):
                npc = quest_models.Quest.CHANI
            elif(npc == "Kang"):
                npc = quest_models.Quest.KANGWOOK
            elif(npc == "Yoon"):
                npc = quest_models.Quest.YOON
            quest = quest_models.Quest.objects.filter(user=user).get(npc=npc)
            reward = quest.problem.reward
            print(reward)
            strawberry = user.strawberry + reward
            quest.is_solved = True
            quest.save()
            user.strawberry = strawberry
            user.save()
            return HttpResponse("QuestSolved")
        except:
            return HttpResponse("UserNotExist")
