# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import Ad

from tutor.serializers import AdSerializer

#获取广告信息
@api_view(['GET'])#请求方式装饰器，只接受get请求
def list_api(request):
    if request.method == 'GET':
        ads = Ad.objects.all().order_by('-create_time')#对象列表
        serializer = AdSerializer(ads, many=True)#对象类型转换成需要的格式json
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

#创建广告
@api_view(['POST'])#只接受post请求
@authentication_classes([AdminTokenAuthtication])#管理员身份认证
def create(request):
    serializer = AdSerializer(data=request.data)#反序列化
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)

    return APIResponse(code=1, msg='创建失败')

#修改广告
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        #数值为空，赋默认值-1
        pk = request.GET.get('id', -1)
        ad = Ad.objects.get(pk=pk)
    except Ad.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = AdSerializer(ad, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='更新失败')

#删除广告
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Ad.objects.filter(id__in=ids_arr).delete()
    except Ad.DoesNotExist:
        return APIResponse(code=1, msg='广告不存在')

    return APIResponse(code=0, msg='删除成功')
