from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.serializers import EventSerializer

# Create your views here.
class ProductApiVeiw(APIView):
    def get(self, request):
        return Response({'mssage': 'get_success'})

    #이벤트 생성
    def post(self, request):
        serialized_event_data = EventSerializer(data=request.data)
        if serialized_event_data.is_valid():
            serialized_event_data.save()
            return Response({'mssage': 'post_success'})

        return Response({'mssage': 'post_fail'}, status=status.HTTP_400_BAD_REQUEST)

    #이벤트 수정
    def put(self, request):
        return Response({'msg': 'put success'})