from rest_framework import serializers
from blog.serializers import ArticleSerializer

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from blog.models import Article as ArticleModel

class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = UserProfileModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "password", "fullname", "email", "userprofile"]
        extra_kwargs = {
            'password':{'write_only':True},
        }