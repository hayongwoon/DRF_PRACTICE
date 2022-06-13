from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article


# Create your views here.
class BlogApiVeiw(APIView):
    #로그인 한 사용자 게시글 정보 보여주는 view
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({'message': 'get method!!'})

