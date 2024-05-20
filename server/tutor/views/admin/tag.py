# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from tutor import utils
from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import Tag
from tutor.serializers import TagSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('-create_time')
        serializer = TagSerializer(tags, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
   

    tags = Tag.objects.filter(title=request.data['title'])
    if len(tags) > 0:
        return APIResponse(code=1, msg='该名称已存在')

    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
   

    try:
        pk = request.GET.get('id', -1)
        tags = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = TagSerializer(tags, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
   

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Tag.objects.filter(id__in=ids_arr).delete()
    except Tag.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    return APIResponse(code=0, msg='删除成功')
