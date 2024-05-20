# Create your views here.
from rest_framework.decorators import api_view

from tutor.handler import APIResponse
from tutor.models import Ad

from tutor.serializers import AdSerializer

#获取轮播图信息
@api_view(['GET'])#请求方式装饰器，只接受get请求
def list_api(request):
    if request.method == 'GET':
        ads = Ad.objects.all().order_by('-create_time')#对象列表
        serializer = AdSerializer(ads, many=True)#对象类型转换成需要的格式json
        return APIResponse(code=0, msg='查询成功', data=serializer.data)