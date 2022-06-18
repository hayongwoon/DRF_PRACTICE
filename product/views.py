from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductApiVeiw(APIView):
    def get(self, request):
        return Response({'mssage': 'get_success'})

    def post(self, request):
        return Response({'mssage': 'post_success'})