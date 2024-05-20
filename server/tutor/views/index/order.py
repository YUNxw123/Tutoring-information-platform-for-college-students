# Create your views here.
from django.db import connection
from rest_framework.decorators import api_view, authentication_classes

from tutor import utils
from tutor.handler import APIResponse
from tutor.models import Classification, Order, Tag, User
from tutor.serializers import OrderSerializer, ClassificationSerializer, ListOrderSerializer, DetailOrderSerializer, \
    UpdateOrderSerializer
from tutor.utils import dict_fetchall
from datetime import datetime

@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        u = request.GET.get("username", None)
        sort = request.GET.get("sort", 'recent')
        print(type(tag))
        # 排序方式
        order = '-create_time'
        if sort == 'recent':
            order = '-create_time'
        elif sort == 'hot' or sort == 'recommend':
            order = '-pv'

        if keyword:
            orders = Order.objects.filter(user__username__contains=keyword).filter(status='0').order_by(order)
        elif u:
            orders = Order.objects.filter(user__username__contains=u).filter().order_by(order)
        else:
            if c and int(c)> -1 and tag:
                # print(1)
                cids = [c]
                tid_arr = tag.split(',')
                print(tid_arr)
                tags= Tag.objects.prefetch_related('tag_orders').filter(id__in=tid_arr)
                tag = tags.values_list('tag_orders__id')
                orders = Order.objects.filter(status='0',id__in=tag,classification_id__in=cids).order_by(order)
            # todo
            elif (c and int(c) == -1) or tag:
                # print(2)
                tid_arr = tag.split(',')
                print(tid_arr)
                tags= Tag.objects.prefetch_related('tag_orders').filter(id__in=tid_arr)
                tag = tags.values_list('tag_orders__id')
                orders = Order.objects.filter(status='0',id__in=tag).order_by(order)
            elif c and int(c) > -1:
                # print(3)
                ids = [c]
                orders = Order.objects.filter(classification_id__in=ids).filter(status='0').order_by(order)
            else:
                # print(4)
                orders = Order.objects.all().filter(status='0').order_by(order)

        serializer = ListOrderSerializer(orders, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
        order.pv = order.pv + 1
        order.save()
    except Order.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        serializer = DetailOrderSerializer(order)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def increaseWishCount(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
        # wish_count加1
        order.wish_count = order.wish_count + 1
        order.save()
    except Order.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    serializer = OrderSerializer(order)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)
#

@api_view(['POST'])
def increaseRecommendCount(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
        # recommend_count加1
        order.recommend_count = order.recommend_count + 1
        order.save()
    except Order.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    serializer = OrderSerializer(order)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)


@api_view(['POST'])
def addWishUser(request):
    try:
        username = request.GET.get('username', None)
        orderId = request.GET.get('orderId', None)

        if username and orderId:
            user = User.objects.get(username=username)
            order = Order.objects.get(pk=orderId)

            if user not in order.wish.all():
                order.wish.add(user)
                order.wish_count += 1
                order.save()

    except Order.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    serializer = OrderSerializer(order)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)


@api_view(['POST'])
def removeWishUser(request):
    try:
        username = request.GET.get('username', None)
        orderId = request.GET.get('orderId', None)

        if username and orderId:
            user = User.objects.get(username=username)
            order = Order.objects.get(pk=orderId)

            if user in order.wish.all():
                order.wish.remove(user)
                order.wish_count -= 1
                order.save()

    except Order.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    return APIResponse(code=0, msg='操作成功')


@api_view(['GET'])
def getWishorderList(request):
    try:
        username = request.GET.get('username', None)
        if username:
            user = User.objects.get(username=username)
            orders = user.wish_orders.all()
            serializer = ListOrderSerializer(orders, many=True)
            return APIResponse(code=0, msg='操作成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='username不能为空')

    except Exception as e:
        utils.log_error(request, '操作失败' + str(e))
        return APIResponse(code=1, msg='获取心愿单失败')


@api_view(['GET'])
def list_user_order_api(request):
    if request.method == 'GET':
        user = request.GET.get("user", None)
        oid = request.GET.get("oid", None)
        if user:
            orders = Order.objects.filter(user=user,id=oid)
            serializer = ListOrderSerializer(orders, many=True)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='user不能为空')


@api_view(['POST'])
def create(request):
    data = request.data.copy()
    data['status'] = '2'
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
def update(request):
    over = request.GET.get('over', None)
    if over:
        try:
            orderId = request.GET.get('id', None)
            print(orderId)
            if orderId:
                order = Order.objects.get(pk=orderId)
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                order.status='3'
                order.over_time=time
                print(order.over_time)
                order.save()
                return APIResponse(code=0, msg='查询成功')
        except Order.DoesNotExist:
            utils.log_error(request, '操作失败')
            return APIResponse(code=1, msg='操作失败')
    else:
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
def delete(request):
    try:
        ids = request.GET.get('id')
        Order.objects.filter(id=ids).delete()
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='删除成功')