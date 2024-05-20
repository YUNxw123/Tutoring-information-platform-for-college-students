from rest_framework.throttling import AnonRateThrottle

#匿名用户访问次数限制：
class MyRateThrottle(AnonRateThrottle):
    THROTTLE_RATES = {"anon": "5/min"}#每分钟5次
