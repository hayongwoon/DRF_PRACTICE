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

    # 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정
    # 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 설정
    def post(self, request):
        return Response({'message': 'post method!!'})