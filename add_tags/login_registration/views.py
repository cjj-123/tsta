from django.http import JsonResponse
from django.shortcuts import render
import hashlib
import time
import jwt
import json
# Create your views here.
from add_tags.settings import SALT, staff
from django.views.decorators.csrf import csrf_exempt
"""
注意： 测试使用，正式只用后，该部分删除
"""


# 判断条款是否被接受
from login_registration.views_model.clause import ClauseModel
from login_registration.views_model.token_model import TokenModel
from login_registration.views_model.request_meta import RequestMeta
clauseModel = ClauseModel()
tokenModel = TokenModel()
requestMeta = RequestMeta()


# 未封装，需要代码示例
@csrf_exempt
def login_logic(request):
    meta = request.META.get('REQUEST_METHOD')
    if meta == 'POST':
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            user_info = staff.find_one({'name': user_name})
            if user_info:
                md5 = hashlib.md5()
                password = password + SALT
                md5.update(password.encode())
                password = md5.hexdigest()
                if password == user_info.get('password'):
                    payload = {
                        'exp': time.time() + 60*60*24*12,
                        'username': user_name,
                        'video_id': '',
                        "alg": "HS256",
                        "typ": "JWT"
                    }
                    token = jwt.encode(payload, SALT).decode()
                    if user_info.get('clause'):
                        response = {
                            'error': 0,
                            'reason': '登录成功',
                            'token': token,
                            'clause': 'ok'
                        }
                    else:
                        response = {
                            'error': 0,
                            'reason': '登录成功',
                            'token': token,
                            'clause': 'remove'
                        }
                    return JsonResponse(response)
                else:
                    response = {
                        'error': 1,
                        'reason': '用户名或密码错误',
                        'token': ''
                    }
                    return JsonResponse(response)
            else:
                response = {
                    'error': 1,
                    'reason': '用户名或密码错误',
                    'token': ''
                }
                return JsonResponse(response)
    else:
        response = {
            'error': 1,
            'reason': '请求类型错误',
            'token': ''
        }
        return JsonResponse(response)


@csrf_exempt
def register_logic(request):
    meta = request.META.get('REQUEST_METHOD')
    if meta == 'POST':
        try:
            receive_data = json.loads(request.body.decode())
            user_name = receive_data.get('username')
            print(user_name)
            if staff.find_one({'name': user_name}):
                response = {
                    'error': 1,
                    'reason': '用户名已存在。',
                    'token': ''
                }
                return JsonResponse(response)
            password = receive_data.get('password')
            if not user_name or not password:
                response = {
                    'error': 1,
                    'reason': '用户名或密码为空。',
                    'token': ''
                }
                return JsonResponse(response)

            md5 = hashlib.md5()
            password = password+SALT
            md5.update(password.encode())
            password = md5.hexdigest()
            print(password)
            staff.insert({'name': user_name, 'password': password})
            response = {
                'error': 0,
                'reason': '注册成功。',
                'token': ''
            }
            return JsonResponse(response)
        except Exception as error:
            print(error)
            response = {
                'error': 1,
                'reason': '参数错误',
                'token': ''
            }
            return JsonResponse(response)

    else:
        response = {
            'error': 1,
            'reason': '请求方式错误。',
            'token': ''
        }
        return JsonResponse(response)


def about_clause(request):

    # 确定请求方式
    meta = request.META.get('REQUEST_METHOD')
    if requestMeta.request_get(meta):
        pass
    else:
        data = {
            'error': 1,
            'reason': '请求方式错误'
        }
        return JsonResponse(data)
    # 请求方式正确，进行相应的逻辑判断
    clause = request.GET.get('clause')
    token = request.META.get('HTTP_TOKEN')
    print(token)
    # 通过token获取用户名
    user_name = tokenModel.get_username(token)

    if clause == 'ok':
        # 通过用户名为用户添加授权状态
        code = clauseModel.agree_clause(user_name)
        if code == 'ok':
            data = {
                'error': 0,
                'reason': '授权正确'
            }
        elif code == 'error':
            data = {
                'error': 1,
                'reason': '授权失败'
            }
        else:
            data = {
                'error': 1,
                'reason': '异常授权'
            }
        return JsonResponse(data)
    else:
        data = {
            'error': 1,
            'reason': '授权错误'
        }
        return JsonResponse(data)


