from email import message
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    data = {
        'message': 'success'
    }
    
    return JsonResponse(data)