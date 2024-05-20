#后台管理系统，无使用
from django.contrib import admin

# Register your models here.
from tutor.models import Classification, Thing, Tag, User, Comment

admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Thing)
admin.site.register(User)
admin.site.register(Comment)
