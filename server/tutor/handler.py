from rest_framework.response import Response

# api返回响应数据处理
class APIResponse(Response):
    def __init__(self, code=0, msg='', data=None, status=200, headers=None, content_type=None, **kwargs):
        dic = {'code': code, 'msg': msg}
        if data is not None:
            dic['data'] = data

        dic.update(kwargs)  # 这里使用update
        super().__init__(data=dic, status=status,
                         template_name=None, headers=headers,
                         exception=False, content_type=content_type)
