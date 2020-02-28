from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import jwt
salt = 'kasd.+54d1sasdoasdnfasifnsafn'
class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)

    def process_request(self, request):  # 某一个view
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        headers = request.META
        try:
            token = headers.get('HTTP_TOKEN')
            jwt.decode(token.encode(), salt)
        except Exception as error:
            print(error)
            response = {
                'error': 1,
                'reason': 'token验证失败',
                'data': ''
            }
            return JsonResponse(response)

    def process_response(self, request, response):
        return response

    def process_exception(self, request, ex):  # View中出现异常时执行
        print("exception:", request, ex)
