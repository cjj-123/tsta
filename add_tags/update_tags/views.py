from django.http import JsonResponse

from django.shortcuts import render
import jwt
from add_tags.settings import video_cache, post_douyin, SALT, staff

# 前端页面刷新问题
# 返回video_url ，video_id
def get_sharing_url(request):
    headers = request.META
    token = headers.get('HTTP_TOKEN')
    staff_name = jwt.decode(token.encode(), SALT).get('username')
    if video_cache.get(staff_name):
        video_id = video_cache.get(staff_name).decode()
        # 记录视频获取时间。防止员工未查看视频就提交。
        video_cache.set(video_id, 'ok', 10)
        video_info = post_douyin.find_one({'video_id': video_id})
        response = {
            'error': 0,
            'reason': '数据获取成功。',
            'sharing_url': video_info.get('video_url')
        }
        return JsonResponse(response)
    # 获取没有添加标签，且没有被其他用户选中的内容
    video_info = post_douyin.find({'tags_one': {'$exists': False}, 'status': {'$exists': False}}).sort('video_date')
    video_data = video_info[0]
    #  添加一个状态，确保再次请求不会因为标签为空而被选中(避免数据更新丢失)
    post_douyin.update({'video_id': video_data.get('video_id')}, {'$set': {'status': 1}})
    # 获取的信息存入缓存
    video_id = video_data.get('video_id')
    video_cache.set(staff_name,video_id)
    video_cache.set(video_id, 'ok', 10)
    response = {
        'error': 0,
        'reason': '数据获取成功。',
        'sharing_url': video_data.get('video_url')
    }
    return JsonResponse(response)


def add_tags_one(request):
    headers = request.META
    meta = headers.get('REQUEST_METHOD')
    token = headers.get('HTTP_TOKEN')
    staff_name = jwt.decode(token.encode(), SALT).get('username')
    if meta == 'GET':
            video_id = video_cache.get(staff_name).decode()
            if video_cache.get(video_id):
                #     留下一个漏洞，第一不可提交，第二次就可以（后来者加油修改）
                response = {
                    'error': 1,
                    'reason': '请观看完整内容后，评论提交。'
                }
                return JsonResponse(response)

            tags_one = request.GET.get('tags_one')
            #     判断是否合法 如果标签已经添加，或者添加标签的个数小于2个，判断为非法提交,或video_info不存在
            video_info = post_douyin.find_one({'video_id': video_id})
            if not video_info \
                    or (len(tags_one.split('，')) < 2
                    or tags_one.count('，') == len(tags_one)) \
                    or video_info.get('tags_one') \
                    or ('' in tags_one.split('，')):

                response = {
                    'error': 1,
                    'reason': '非法提交'
                }
            else:
                staff_info = staff.find_one({'name': staff_name})
                if not staff_info.get('tags_all'):
                    staff.update({'name': staff_name}, {'$set': {'tags_all': 0}})
                # 判断用户是否是第一次添加
                if not staff_info.get('tags_new'):
                    staff.update({'name': staff_name}, {'$set': {'tags_new': 0}})
                #     添加标签数量加一
                staff.update({'name': staff_name}, {'$set': {'tags_all': staff_info.get('tags_all')+1}})
                staff.update({'name': staff_name}, {'$set': {'tags_new': staff_info.get('tags_new')+1}})
                # 为视频添加标签（并标注为该视频添加标签的是那个用户）
                post_douyin.update({'video_id': video_id}, {'$set': {'tags_one': tags_one}})
                post_douyin.update({'video_id': video_id}, {'$set': {'username': staff_name}})
                # 取消用户的视频url缓存，使用户可以继续获取新视频的url
                video_cache.delete(staff_name)
                response = {
                    'error': 0,
                    'reason': '提交成功'
                }
    else:
        response = {
            'error': 1,
            'reason': '错误请求。'
        }
    return JsonResponse(response)





