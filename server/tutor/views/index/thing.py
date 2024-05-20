# Create your views here.
from django.db import connection
from rest_framework.decorators import api_view, authentication_classes

from tutor import utils
from tutor.handler import APIResponse
from tutor.models import Classification, Thing, Tag, User
from tutor.serializers import ThingSerializer, ClassificationSerializer, ListThingSerializer, DetailThingSerializer, \
    UpdateThingSerializer
from tutor.utils import dict_fetchall


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        sort = request.GET.get("sort", 'recent')
        print(type(tag))
        # 排序方式
        order = '-create_time'
        if sort == 'recent':
            order = '-create_time'
        elif sort == 'hot' or sort == 'recommend':
            order = '-pv'

        if keyword:
            things = Thing.objects.filter(title__contains=keyword).filter(status='0').order_by(order)
        else:
            if c and int(c)> -1 and tag:
                # print(1)
                cids = [c]
                tid_arr = tag.split(',')
                print(tid_arr)
                tags= Tag.objects.prefetch_related('tag_things').filter(id__in=tid_arr)
                tag = tags.values_list('tag_things__id')
                things = Thing.objects.filter(status='0',id__in=tag,classification_id__in=cids).order_by(order)
            # todo
            elif (c and int(c) == -1)or tag:
                # print(2)
                tid_arr = tag.split(',')
                print(tid_arr)
                tags= Tag.objects.prefetch_related('tag_things').filter(id__in=tid_arr)
                tag = tags.values_list('tag_things__id')
                things = Thing.objects.filter(status='0',id__in=tag).order_by(order)
            elif c and int(c) > -1:
                # print(3)
                ids = [c]
                things = Thing.objects.filter(classification_id__in=ids).filter(status='0').order_by(order)
            else:
                # print(4)
                things = Thing.objects.all().filter(status='0').order_by(order)

        serializer = ListThingSerializer(things, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        thing = Thing.objects.get(pk=pk)
        thing.pv = thing.pv + 1
        thing.save()
    except Thing.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        serializer = ThingSerializer(thing)
        print(1)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


# @api_view(['POST'])
# def increaseWishCount(request):
#     try:
#         pk = request.GET.get('id', -1)
#         thing = Thing.objects.get(pk=pk)
#         # wish_count加1
#         thing.wish_count = thing.wish_count + 1
#         thing.save()
#     except Thing.DoesNotExist:
#         utils.log_error(request, '对象不存在')
#         return APIResponse(code=1, msg='对象不存在')
#
#     serializer = ThingSerializer(thing)
#     return APIResponse(code=0, msg='操作成功', data=serializer.data)
#

@api_view(['POST'])
def increaseRecommendCount(request):
    try:
        pk = request.GET.get('id', -1)
        thing = Thing.objects.get(pk=pk)
        # recommend_count加1
        thing.recommend_count = thing.recommend_count + 1
        thing.save()
    except Thing.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    serializer = ThingSerializer(thing)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)


# @api_view(['POST'])
# def addWishUser(request):
#     try:
#         username = request.GET.get('username', None)
#         thingId = request.GET.get('thingId', None)
#
#         if username and thingId:
#             user = User.objects.get(username=username)
#             thing = Thing.objects.get(pk=thingId)
#
#             if user not in thing.wish.all():
#                 thing.wish.add(user)
#                 thing.wish_count += 1
#                 thing.save()
#
#     except Thing.DoesNotExist:
#         utils.log_error(request, '操作失败')
#         return APIResponse(code=1, msg='操作失败')
#
#     serializer = ThingSerializer(thing)
#     return APIResponse(code=0, msg='操作成功', data=serializer.data)
#
#
# @api_view(['POST'])
# def removeWishUser(request):
#     try:
#         username = request.GET.get('username', None)
#         thingId = request.GET.get('thingId', None)
#
#         if username and thingId:
#             user = User.objects.get(username=username)
#             thing = Thing.objects.get(pk=thingId)
#
#             if user in thing.wish.all():
#                 thing.wish.remove(user)
#                 thing.wish_count -= 1
#                 thing.save()
#
#     except Thing.DoesNotExist:
#         utils.log_error(request, '操作失败')
#         return APIResponse(code=1, msg='操作失败')
#
#     return APIResponse(code=0, msg='操作成功')
#
#
# @api_view(['GET'])
# def getWishThingList(request):
#     try:
#         username = request.GET.get('username', None)
#         if username:
#             user = User.objects.get(username=username)
#             things = user.wish_things.all()
#             serializer = ListThingSerializer(things, many=True)
#             return APIResponse(code=0, msg='操作成功', data=serializer.data)
#         else:
#             return APIResponse(code=1, msg='username不能为空')
#
#     except Exception as e:
#         utils.log_error(request, '操作失败' + str(e))
#         return APIResponse(code=1, msg='获取心愿单失败')
#

@api_view(['POST'])
def addCollectUser(request):
    try:
        username = request.GET.get('username', None)
        thingId = request.GET.get('thingId', None)

        if username and thingId:
            user = User.objects.get(username=username)
            thing = Thing.objects.get(pk=thingId)

            if user not in thing.collect.all():
                thing.collect.add(user)
                thing.collect_count += 1
                thing.save()

    except Thing.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    serializer = DetailThingSerializer(thing)
    return APIResponse(code=0, msg='操作成功', data=serializer.data)


@api_view(['POST'])
def removeCollectUser(request):
    try:
        username = request.GET.get('username', None)
        thingId = request.GET.get('thingId', None)

        if username and thingId:
            user = User.objects.get(username=username)
            thing = Thing.objects.get(pk=thingId)

            if user in thing.collect.all():
                thing.collect.remove(user)
                thing.collect_count -= 1
                thing.save()

    except Thing.DoesNotExist:
        utils.log_error(request, '操作失败')
        return APIResponse(code=1, msg='操作失败')

    return APIResponse(code=0, msg='操作成功')


@api_view(['GET'])
def getCollectThingList(request):
    try:
        username = request.GET.get('username', None)
        if username:
            user = User.objects.get(username=username)
            things = user.collect_things.all()
            serializer = ListThingSerializer(things, many=True)
            return APIResponse(code=0, msg='操作成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='username不能为空')

    except Exception as e:
        utils.log_error(request, '操作失败' + str(e))
        return APIResponse(code=1, msg='获取收藏失败')


@api_view(['GET'])
def list_user_thing_api(request):
    if request.method == 'GET':
        user = request.GET.get("user", None)

        if user:
            things = Thing.objects.filter(user=user)
            serializer = ListThingSerializer(things, many=True)
            return APIResponse(code=0, msg='查询成功', data=serializer.data)
        else:
            return APIResponse(code=1, msg='user不能为空')


@api_view(['POST'])
def create(request):
    data = request.data.copy()
    data['status'] = '1'
    serializer = ThingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        thing = Thing.objects.get(pk=pk)
    except Thing.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = UpdateThingSerializer(thing, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
    else:
        print(serializer.errors)
        utils.log_error(request, '参数错误')

    return APIResponse(code=1, msg='更新失败')
