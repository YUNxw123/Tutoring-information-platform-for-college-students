# Create your views here.
from rest_framework.decorators import api_view

from tutor.handler import APIResponse
from tutor.models import Notice,Thing,Order
from tutor.serializers import NoticeSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        uid = request.GET.get("uid", None)
        print(uid)
        if uid:
            things = Thing.objects.filter(user_id=uid)
            print(things)
            orders = Order.objects.filter(user_id=uid)
            print(orders)
            if things and orders:
                notices = Notice.objects.all().order_by('-create_time')
            elif things:
                notices = Notice.objects.filter(status__in=[0,1]).order_by('-create_time')
            elif orders:
                notices = Notice.objects.filter(status__in=[0,2]).order_by('-create_time')
            else:
                notices = Notice.objects.filter(status=0).order_by('-create_time')
        serializer = NoticeSerializer(notices, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

