# Create your views here.
from django.db import connection
from rest_framework.decorators import api_view

from tutor.handler import APIResponse
from tutor.models import Classification
from tutor.serializers import ClassificationSerializer
from tutor.utils import dict_fetchall
import datetime

@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        classifications = Classification.objects.all().order_by('-create_time')
        serializer = ClassificationSerializer(classifications, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

@api_view(['GET'])
def countlist_api(request):
    if request.method == 'GET':
        now = datetime.datetime.now()

        # 统计分类比例(sql语句)
        sql_str = "select B.id,B.title from b_thing A join b_classification B on " \
                  "A.classification_id = B.id group by B.title order by count desc limit 4; "
        with connection.cursor() as cursor:
            cursor.execute(sql_str)
            classification_rank_data = dict_fetchall(cursor)

        return APIResponse(code=0, msg='查询成功', data=classification_rank_data)





