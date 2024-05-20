import datetime
import hashlib
import time

from tutor.serializers import ErrorLogSerializer

#获取当前时间的毫秒级时间戳
def get_timestamp():
    return int(round(time.time() * 1000))

#计算字符串的md5哈希值，小写输出
def md5value(key):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    md5str = (input_name.hexdigest()).lower()
    # print('计算md5:', md5str)
    return md5str

#封装数据库数据
def dict_fetchall(cursor):  # cursor是执行sql_str后的记录，作入参
    columns = [col[0] for col in cursor.description]  # 得到域的名字col[0]，组成List
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

#获取请求者的ip
def get_ip(request):
    """

    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#获取请求者的IP信息
def get_ua(request):
    """
    """
    ua = request.META.get('HTTP_USER_AGENT')
    return ua[0:200]


def getWeekDays():
    """
    获取近一周的日期
    """
    week_days = []
    now = datetime.datetime.now()
    for i in range(7):
        day = now - datetime.timedelta(days=i)
        week_days.append(day.strftime('%Y-%m-%d %H:%M:%S.%f')[:10])
    week_days.reverse()  # 逆序
    return week_days


def get_monday():
    """
    获取本周周一日期
    """
    now = datetime.datetime.now()
    monday = now - datetime.timedelta(now.weekday())
    return monday.strftime('%Y-%m-%d %H:%M:%S.%f')[:10]


def log_error(request, content):
    """
    记录错误日志
    """
    ip = get_ip(request)
    method = request.method
    url = request.path

    data = {
        'ip': ip,
        'method': method,
        'url': url,
        'content': content
    }

    # 入库
    serializer = ErrorLogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
