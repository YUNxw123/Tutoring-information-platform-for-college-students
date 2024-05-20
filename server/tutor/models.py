from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ('1', '管理员'),
        ('2', '普通用户'),
    )
    STATUS_CHOICES = (
        ('0', '正常'),
        ('1', '封号'),
    )
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=2,  choices=ROLE_CHOICES, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.FileField(upload_to='avatar/', null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    description = models.TextField(max_length=200, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    admin_token = models.CharField(max_length=32, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = "b_user"


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_tag"


class Classification(models.Model):
    list_display = ("title", "id")
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "b_classification"


class Thing(models.Model):
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
        ('2', '待审核'),
    )
    id = models.BigAutoField(primary_key=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='classification_thing')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_thing')
    #多对多
    tag = models.ManyToManyField(Tag, blank=True,related_name='tag_things')
    title = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=4, blank=True, null=True)
    cert = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='2')
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    pv = models.IntegerField(default=0)#浏览次数
    collect = models.ManyToManyField(User, blank=True, related_name="collect_things")
    collect_count = models.IntegerField(default=0)

    class Meta:
            db_table = "b_thing"

# #
# class Wish(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_record')
#     thing = models.ForeignKey(Thing, on_delete=models.CASCADE, null=True, related_name='thing_record')
#     record_time = models.DateTimeField(auto_now_add=True, null=True)
#
#     class Meta:
#         db_table = "b_wish"

#登录日志
class LoginLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    ua = models.CharField(max_length=200, blank=True, null=True)
    log_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_login_log"

#操作日志
class OpLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    re_ip = models.CharField(max_length=100, blank=True, null=True)
    re_time = models.DateTimeField(auto_now_add=True, null=True)
    re_url = models.CharField(max_length=200, blank=True, null=True)
    re_method = models.CharField(max_length=10, blank=True, null=True)
    re_content = models.CharField(max_length=200, blank=True, null=True)
    access_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "b_op_log"

#错误日志
class ErrorLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=10, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    log_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_error_log"

##需求
class Order(models.Model):
    STATUS_CHOICES = (
        ('0', '上架'),
        ('1', '下架'),
        ('2', '待审核'),
        ('3', '已结束'),
    )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_order')
    # thing = models.ManyToManyField(Thing, blank=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='classification_order')
    tag = models.ManyToManyField(Tag, blank=True,related_name='tag_orders')
    description = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='2')
    price = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    wish = models.ManyToManyField(User, blank=True, related_name="wish_orders")
    wish_count = models.IntegerField(default=0)
    pv = models.IntegerField(default=0)#浏览次数
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    over_time = models.DateTimeField(null=True)

    class Meta:
        db_table = "b_order"

#评论
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_comment')
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, null=True, related_name='thing_comment')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='order_comment')
    comment_time = models.DateTimeField(auto_now_add=True, null=True)
    like_count = models.IntegerField(default=0)

    class Meta:
        db_table = "b_comment"

#横幅
class Ad(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='ad/', null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_ad"

#消息提醒
class Notice(models.Model):
    STATUS_CHOICES = (
        ('0', '全部用户'),
        ('1', '家教用户'),
        ('2', '需求用户'),
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    user = models.ManyToManyField(User,blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "b_notice"
