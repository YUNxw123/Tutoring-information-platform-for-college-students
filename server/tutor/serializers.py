from rest_framework import serializers

from tutor.models import Thing, Classification, Tag, User, Comment, LoginLog, Order,OpLog, \
    Ad, Notice, ErrorLog

#序列化->模型类的数据转化成json类数据
#标签
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#家教所有信息
class ThingSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        #序列化的模型
        model = Thing
        #序列化的字段
        fields = '__all__'
#家教详情信息
class DetailThingSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')
    class Meta:
        model = Thing
        # 排除多对多字段
        exclude = ('collect',)

#修改家教信息
class UpdateThingSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Thing
        # 排除多对多字段
        exclude = ('collect',)

#查询家教信息
class ListThingSerializer(serializers.ModelSerializer):
    # 额外字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Thing
        # 排除字段
        exclude = ('collect',)

#分类
class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'



#用户
class UserSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ('password',)

#评论信息
class CommentSerializer(serializers.ModelSerializer):
    comment_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # 额外字段
    title = serializers.ReadOnlyField(source='thing.title')
    username = serializers.ReadOnlyField(source='user.username')
    ordername = serializers.ReadOnlyField(source='order.user.username')
    class Meta:
        model = Comment
        fields = '__all__'





class LoginLogSerializer(serializers.ModelSerializer):
    log_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = LoginLog
        fields = '__all__'


class OpLogSerializer(serializers.ModelSerializer):
    re_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = OpLog
        fields = '__all__'


class ErrorLogSerializer(serializers.ModelSerializer):
    log_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = ErrorLog
        fields = '__all__'

#需求
class OrderSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    over_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    username = serializers.ReadOnlyField(source='user.username')
    classification_title = serializers.ReadOnlyField(source='classification.title')
    thing_title = serializers.ReadOnlyField(source='thing.title')

    class Meta:
        model = Order
        fields = '__all__'

class DetailOrderSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    over_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    username = serializers.ReadOnlyField(source='user.username')
    userrole = serializers.ReadOnlyField(source='user.role')
    useravatar = serializers.FileField(source='user.avatar')
    classification_title = serializers.ReadOnlyField(source='classification.title')


    class Meta:
        model = Order
        # 排除多对多字段
        exclude = ('wish',)


class UpdateOrderSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    over_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    username = serializers.ReadOnlyField(source='user.username')
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Order
        # 排除多对多字段
        exclude = ('wish',)


class ListOrderSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    over_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    username = serializers.ReadOnlyField(source='user.username')
    userrole = serializers.ReadOnlyField(source='user.role')
    useravatar = serializers.FileField(source='user.avatar')
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Order
        # 排除字段
        exclude = ('wish',)


#广告
class AdSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Ad
        fields = '__all__'

#消息
class NoticeSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Notice
        fields = '__all__'

