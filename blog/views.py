from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from rest_framework import status
from blog.serializers import ArticleSerializer
from user.serializers import UserSerializer


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
        return Response({'message': 'post method!!'})