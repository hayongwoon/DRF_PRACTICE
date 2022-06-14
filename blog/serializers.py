from rest_framework import serializers

from blog.models import Article as ArticleModel
from user.models import User as UserModel


#작성자 시리얼라이저를 만든다.
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email']

class ArticleSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()
    class Meta:
        # serializer에 사용될 model, field지정
        model = ArticleModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

