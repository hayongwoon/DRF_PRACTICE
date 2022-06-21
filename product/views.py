from functools import partial
from itertools import product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.serializers import EventSerializer
from product.models import Event as EventModel
from datetime import datetime

# Create your views here.
class ProductApiVeiw(APIView):
    #현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 활성화 여부가 True인 event 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요
    def get(self, request):
        now = datetime.now()
        exposure_events = EventModel.objects.filter(start_propose_date__lte=now, end_propose_date__gte=now, is_active=True) 
        serialized_exposure_events = EventSerializer(exposure_events, many=True).data
        return Response(serialized_exposure_events, status=status.HTTP_200_OK)

    #이벤트 생성
    def post(self, request):
        serialized_event_data = EventSerializer(data=request.data)
        if serialized_event_data.is_valid():
            serialized_event_data.save()
            return Response(serialized_event_data.data, status=status.HTTP_200_OK)

        return Response(serialized_event_data.errors, status=status.HTTP_400_BAD_REQUEST)

    #이벤트 수정
    def put(self, request, obj_id):
        product = EventModel.objects.get(id=obj_id)
        serialized_event_data = EventSerializer(product, data=request.data, partial=True)
        if serialized_event_data.is_valid():
            serialized_event_data.save()

            return Response(serialized_event_data.data, status=status.HTTP_200_OK)

        return Response(serialized_event_data.errors, status=status.HTTP_400_BAD_REQUEST)