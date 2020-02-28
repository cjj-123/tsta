from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
# 获取用户标签添加信息
from login_registration.views_model.token_model import TokenModel
from data_manager.data_models.staff_add_tags_info import TagsInfo
tagsInfo = TagsInfo()
tokenModel = TokenModel()


def get_tags(request):
    token = request.META.get('HTTP_TOKEN')
    user_name = tokenModel.get_username(token)
    tags_info = tagsInfo.get_tags(user_name)
    return JsonResponse(tags_info)


# 结算对应的标签数量（username,number）用户名，结算数量
def update_tags(request):
    headers = request.META
    meta = headers.get('REQUEST_METHOD')
    if meta.lower() == 'post':
        data = request.body.decode()
        data = json.dumps(data)
        user_name = data.get('username')
        number = data.get('number')
        data = tagsInfo.update_tags(user_name, number)
        return JsonResponse(data)
    else:
        data = {
            'error': 1,
            'reason': '请求方式有误。'
        }
        return JsonResponse(data)


# 获取标签提示
def label_prompt(request):
    meta = request.META.get('REQUEST_METHOD')
    if meta.lower() == "get":
        key_word = request.GET.get('keyword')
        # print(key_word)
        key_word = key_word.split('，')[-1]
        print(key_word)
        label_list = tagsInfo.label_recommendation(key_word)
        data = {
            'error': 0,
            'reason': '数据正常',
            'data': label_list
        }
        return JsonResponse(data)
    else:
        data = {
            'error': 1,
            'reason': '请求方式有误',
            'data': []
        }
        return JsonResponse(data)



