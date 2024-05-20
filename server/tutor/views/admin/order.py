# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from tutor import utils
from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import Classification, Order, Tag,User
from tutor.serializers import OrderSerializer, UpdateOrderSerializer

#查询（）
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        search_type= request.GET.get("search_type", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        print(keyword)
        print(search_type)
        if keyword:
            if (search_type == 'n'):
                orders = Order.objects.filter(user__username__contains=keyword).order_by('create_time')
            elif (search_type == 'c'):
                orders = Order.objects.filter(classification__title__contains=keyword).order_by('create_time')
            elif (search_type == 't'):
                orders = Order.objects.filter(tag__title__contains=keyword).order_by('create_time')
        elif c:
            classification = Classification.objects.get(pk=c)
            orders = classification.classification_order.all()
        elif tag:
            tag = Tag.objects.get(id=tag)
            print(tag)
            orders = tag.order_set.all()
        else:
            orders = Order.objects.all().order_by('create_time')

        serializer = OrderSerializer(orders, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

@api_view(['GET'])
def auditlist_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        search_type= request.GET.get("search_type", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        print(keyword)
        print(search_type)
        if keyword:
            if (search_type == 'n'):
                orders = Order.objects.filter(status='2',title__contains=keyword).order_by('create_time')
            elif (search_type == 'c'):
                orders = Order.objects.filter(status='2',classification__title__contains=keyword).order_by('create_time')
            elif (search_type == 't'):
                orders = Order.objects.filter(status='2',tag__title__contains=keyword).order_by('create_time')
        elif c:
            classification = Classification.objects.get(pk=c)
            orders = classification.classification_order.all(status='2')
        elif tag:
            tag = Tag.objects.get(id=tag)
            print(tag)
            orders = tag.order_set.filter(status='2')
        else:
            orders = Order.objects.filter(status='2').order_by('create_time')

        serializer = OrderSerializer(orders, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)



#详情
@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = UpdateOrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Order.objects.filter(id__in=ids_arr).delete()
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='删除成功')

@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def audit_pass(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        type = request.GET.get('type')
        if (type=='1'):
            Order.objects.filter(id__in=ids_arr).update(status=0)
        elif (type == '2'):
            Order.objects.filter(id__in=ids_arr).update(status=1)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='审核成功')
