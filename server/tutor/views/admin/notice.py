# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import Notice

from tutor.serializers import NoticeSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        notices = Notice.objects.all().order_by('-create_time')
        serializer = NoticeSerializer(notices, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
   

    serializer = NoticeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        notice = Notice.objects.get(pk=pk)
    except Notice.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = NoticeSerializer(notice, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Notice.objects.filter(id__in=ids_arr).delete()
    except Notice.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    return APIResponse(code=0, msg='删除成功')
