# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import Comment

from tutor.serializers import CommentSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        type= request.GET.get("type", None)
        if (type == 't'):
            if keyword:
                comments = Comment.objects.filter(thing__isnull=False,thing__title__contains=keyword).order_by('create_time')
            else:
                comments = Comment.objects.filter(thing__isnull=False).order_by('-comment_time')
        elif (type == 'd'):
            if keyword:
                comments = Comment.objects.filter(order__isnull=False,user__username__contains=keyword).order_by('create_time')
            else:
                comments = Comment.objects.filter(order__isnull=False).order_by('-comment_time')
        # print(comments)
        serializer = CommentSerializer(comments, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        comments = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = CommentSerializer(comments, data=request.data)
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
        Comment.objects.filter(id__in=ids_arr).delete()
    except Comment.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    return APIResponse(code=0, msg='删除成功')
