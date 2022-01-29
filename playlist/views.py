from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import authentication, permissions 
from django.http import JsonResponse

def main(request):
    like = 0
    like = like + 1
    context = {
        "land_type":"about",
        "name": "arsen",
        "id": 6,
    }
    return render(request, "index.html", context)
    
def about(request):
    context = {
        "id": 6,
    }
    return render(request, "playlist.html", context)
    