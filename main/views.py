import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.core import serializers

from main.lib import find_dishes


def index(request):
    return render(request, "main/index.html")


def add(request):
    return render(request, "main/add.html") 


def get_recipy(request: HttpRequest):
    return HttpResponse(find_dishes(json.loads(request.body)))
