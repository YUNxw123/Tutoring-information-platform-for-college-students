# Create your views here.
import datetime

from rest_framework.decorators import api_view, authentication_classes

from tutor import utils
from tutor.auth.authentication import AdminTokenAuthtication
from tutor.handler import APIResponse
from tutor.models import User
from tutor.serializers import UserSerializer, LoginLogSerializer
from tutor.utils import md5value

#生成登录日志
def make_login_log(request):
    try:
        username = request.data['username']
        data = {
            "username": username,
            "ip": utils.get_ip(request),
            "ua": utils.get_ua(request)
        }
        serializer = LoginLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
    except Exception as e:
        print(e)

#管理员登录
@api_view(['POST'])
def admin_login(request):
    username = request.data['username']
    password = utils.md5value(request.data['password'])

    users = User.objects.filter(username=username, password=password, role__in=['1'])
    if len(users) > 0:
        user = users[0]
        data = {
            'username': username,
            'password': password,
            'admin_token': md5value(username)  # 生成令牌
        }
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            make_login_log(request)
            return APIResponse(code=0, msg='登录成功', data=serializer.data)
        else:
            print(serializer.errors)

    return APIResponse(code=1, msg='用户名或密码错误')

#获取用户信息
@api_view(['GET'])
def info(request):
    if request.method == 'GET':
        pk = request.GET.get('id', -1)
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

#关键字查询用户信息
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", '')
        users = User.objects.filter(username__contains=keyword).order_by('-create_time')
        serializer = UserSerializer(users, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

#创建账号
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
   

    print(request.data)
    if not request.data.get('username', None) or not request.data.get('password', None):
        return APIResponse(code=1, msg='用户名或密码不能为空')
    users = User.objects.filter(username=request.data['username'])
    if len(users) > 0:
        return APIResponse(code=1, msg='该用户名已存在')

    data = request.data.copy()
    data.update({'password': utils.md5value(request.data['password'])})
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='创建失败')

#修改用户信息
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
#删除用户名和密码，因为只读，不能传入修改
    data = request.data.copy()
    if 'username' in data.keys():
        del data['username']
    if 'password' in data.keys():
        del data['password']
    serializer = UserSerializer(user, data=data)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        print(serializer.errors)
    return APIResponse(code=1, msg='更新失败')

#修改用户密码
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def updatePwd(request):

    try:
        pk = request.GET.get('id', -1)
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    password = request.data.get('password', None)
    newPassword1 = request.data.get('newPassword1', None)
    newPassword2 = request.data.get('newPassword2', None)

    if not password or not newPassword1 or not newPassword2:
        return APIResponse(code=1, msg='不能为空')

    if user.password != utils.md5value(password):
        return APIResponse(code=1, msg='原密码不正确')

    if newPassword1 != newPassword2:
        return APIResponse(code=1, msg='两次密码不一致')

    data = request.data.copy()
    data.update({'password': utils.md5value(newPassword1)})
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='更新失败')

#删除用户信息
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
   

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        User.objects.filter(id__in=ids_arr).delete()
    except User.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    return APIResponse(code=0, msg='删除成功')
