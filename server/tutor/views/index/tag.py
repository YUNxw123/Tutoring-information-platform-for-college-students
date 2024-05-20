# Create your views here.
from rest_framework.decorators import api_view

from tutor.handler import APIResponse
from tutor.models import Tag,Classification
from tutor.serializers import TagSerializer

from django.db import connection
from tutor.utils import dict_fetchall
import datetime

@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('-create_time')
        serializer = TagSerializer(tags, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('-create_time')
        serializer = TagSerializer(tags, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

@api_view(['GET'])
def countlist_api(request):
    if request.method == 'GET':
        try:
            ids = request.GET.get('tid')
            print(ids)
            tags=Tag.objects.filter(id__in=ids)
        except Tag.DoesNotExist:
            return APIResponse(code=1, msg='对象不存在')
        serializer = TagSerializer(tags, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)



