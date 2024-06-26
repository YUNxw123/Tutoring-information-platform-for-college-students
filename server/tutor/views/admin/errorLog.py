# Create your views here.
from rest_framework.decorators import api_view

from tutor.handler import APIResponse
from tutor.models import ErrorLog
from tutor.serializers import ErrorLogSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        errorLogs = ErrorLog.objects.all().order_by('-log_time')
        serializer = ErrorLogSerializer(errorLogs, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
