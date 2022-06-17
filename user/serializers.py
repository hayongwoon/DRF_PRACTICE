from django.urls import is_valid_path
from rest_framework import serializers
from blog.serializers import ArticleSerializer

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from blog.models import Article as ArticleModel

class HobbySerializer(serializers.ModelSerializer):
    people_with_my_hobby = serializers.SerializerMethodField()
    #get_변수이름 으로 함수 선언하면 해당 함수의 리턴값이 해당 변수를 참조하게 되고 필드로 설정할 수 있음. 
    # 역참조를 불러오기 위해선 해당 객체를 받아와서 각 객체마다의 정보를 가져와야한다. 때문에 함수를 선언하여 리턴값을 불러와 필드로 지정할 수 있는 serializers.SerializerMethodField() 활용
    def get_people_with_my_hobby(self, obj): 
        #취미 객체로 부터 자신을 참조하고있는 모든 프로필을 가져오고 그 프로필의 유저네임을 가져온다.
        #나를 제외하고 가져올 수는 없을까...? exclude(user=user)를 사용하려면 hobby의 객체들의 근원지인 user를 가져와야하는데....
        return [user_profile.user.fullname for user_profile in obj.userprofile_set.exclude(user=self.context['request'].user)]

    class Meta:
        # serializer에 사용될 model, field지정
        model = HobbyModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["name", "people_with_my_hobby"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)

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