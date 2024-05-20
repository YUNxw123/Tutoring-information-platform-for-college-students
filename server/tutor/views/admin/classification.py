# Create your views here.
from django.db import connection
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes

from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import Classification

from tutor.serializers import ClassificationSerializer
from tutor.utils import dict_fetchall


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        classifications = Classification.objects.all().order_by('-create_time')
        serializer = ClassificationSerializer(classifications, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
    classification = Classification.objects.filter(title=request.data['title'])
    if len(classification) > 0:
        return APIResponse(code=1, msg='该名称已存在')

    serializer = ClassificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        print(pk)
        classification = Classification.objects.get(pk=pk)
    except Classification.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = ClassificationSerializer(classification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        # 删除自身和自身的子孩子
        Classification.objects.filter(Q(id__in=ids_arr)).delete()
    except Classification.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='删除成功')
