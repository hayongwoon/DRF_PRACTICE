from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import User, Hobby, UserProfile
from django.db.models import Count, F, Value
from django.contrib.auth import authenticate, login
from rest_framework import status
from blog.models import Article
from user.serializers import UserSerializer

# Permission custom
class BronzeRank(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and
            request.user.user_rank >= 1
            )

class UserView(APIView): # CBV 방식
    # permission_classes = [BronzeRank]
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        user = User.objects.get(id=5)
        hobbys = list(user.userprofile.hobby.all())
        
        # dir()과 eval()을 통한 user와 관련된 메소드 도출!
        # for command in dir(user):
        #     try:
        #         print(f'user.{command} :', eval(f'user.{command}'))
        #     except:
        #         pass
                
        for hobby in hobbys:
            # exclde : 매칭 된 쿼리만 제외, filter와 반대
            # annotate : 필드 이름을 변경해주기 위해 사용, 이외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
            # values / values_list : 지정한 필드만 리턴 할 수 있음. values는 dict로 return, values_list는 tuple로 ruturn
            # F() : 객체에 해당되는 쿼리를 생성함
            hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
            print(str(hobby_members.query))
            # print(hobby.userprofile_set)
            # print(hobby.userprofile_set.all())
            # print(hobby.userprofile_set.exclude(user=user))
            # print(hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')))
            # print(hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True))
            # print(f"hobby : {hobby.name} / hobby members : {hobby_members}")

        return Response({'message': 'get method!!'})
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})


class UserApiView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


    # 로그인 한 유저의 모든 정보
    def get(self, request):
        user = request.user
        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        serialized_user_data = UserSerializer(user, context={'request':request}).data
        return Response(serialized_user_data, status=status.HTTP_200_OK)
    