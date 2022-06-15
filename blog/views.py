from unicodedata import name
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article, Category
from rest_framework import status
from blog.serializers import ArticleSerializer
from blog.services.article_service import create_an_article
from user.models import User
from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone

# Permission custom
# 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한
class RegistedMoreThan3daysUser(BasePermission):
    """
    가입일 기준 1주일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 1주일 이상 지난 사용자만 사용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3)))


# Create your views here.
class BlogApiVeiw(APIView):
    # 로그인 한 사용자의 정보와 게시글을 보여주는 기능
    def get(self, request):
        articles = Article.objects.all()        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        serialized_article_data = ArticleSerializer(articles, many=True).data

        return Response(serialized_article_data, status=status.HTTP_200_OK)

    # 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정
    # 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 설정
    def post(self, request):
        # permission_classes = [permissions.RegistedMoreThan3daysUser]
        try:
            create_an_article(title=request.data.get('title'),
                           user_id=User.objects.get(id=5), # 우선 로그인한 유저를 해장 값으로 설정해보자.
                           content=request.data.get('content'),
                           category=request.data.get('category'),) #외래키일 경우 
                           
            return Response({'result': '게시글이 생성 되었습니다.'}, status=status.HTTP_201_CREATED)

        except TypeError:
            return Response({'msg': "항목을 다시 확인 해 주세요."}, status=status.HTTP_404_NOT_FOUND)