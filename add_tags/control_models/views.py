from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import pymongo
connect = pymongo.MongoClient(host='localhost', port=27017)
db = connect.shangjing
staff_collection = db.staff
shangol_collection = db.shangol
staff_shangol_map = db.staff_shangol_map
post_douyin = db.post_douyin
"""
[{'_id': ObjectId('5e2000f68fe59e882fb0ff4b'), 'name': 'cao', 'password': '726eb528f32e7a9f2c9f628c9f7e3d1f'}]

[{'_id': ObjectId('5e200074e4c0c1f1212bcb74'), 'post_douyin': 1, 'name': '贝乐泰', 'id': 98492270062}, {'_id': ObjectId('5e200074e4c0c1f1212bcb89'), 'post_douyin': 1, 'name': '夏波波Brian', 'id': 80745032657}, {'_id': ObjectId('5e200074e4c0c1f1212bcba1'), 'post_douyin': 1, 'name': '歪果仁研究协会', 'id': 84838275326}, {'_id': ObjectId('5e200074e4c0c1f1212bcbb6'), 'post_douyin': 1, 'name': '西班牙小哥儿德明', 'id': 95040145160}, {'_id': ObjectId('5e200074e4c0c1f1212bcbcb'), 'post_douyin': 1, 'name': '口语老炮儿马思瑞', 'id': 68001314839}, {'_id': ObjectId('5e200074e4c0c1f1212bcbe0'), 'post_douyin': 1, 'name': '穆雷中财', 'id': 86462745631}, {'_id': ObjectId('5e200074e4c0c1f1212bcbf2'), 'post_douyin': 1, 'name': '星悦小美女PKU', 'id': 82837571567}, {'_id': ObjectId('5e200074e4c0c1f1212bcc07'), 'post_douyin': 1, 'name': '万国土特产', 'id': 95353972682}, {'_id': ObjectId('5e20007fe4c0c1f1212c1d5b'), 'post_douyin': 1, 'name': '俏奶奶二人组', 'id': 68354827719}, {'_id': ObjectId('5e20007fe4c0c1f1212c1d67'), 'post_douyin': 1, 'name': '大静奋斗ing', 'id': 2334997990873040}, {'_id': ObjectId('5e20007fe4c0c1f1212c1d74'), 'post_douyin': 1, 'name': '好获严选', 'id': 3003501057414970}]

"""

def choice_object(request):
    staff_id = set()
    shangol_id = set()
    staff_list = []
    shangol_list = []
    map_relation_data = staff_shangol_map.find()
    staff_data= staff_collection.find()
    shangol_data = shangol_collection.find()
    for map in map_relation_data:
        pass
        # staff_id.add(map.get('staff_id'))
        # shangol_id.add(map.get('shangol_id'))

    for staff in staff_data:
        if staff.get('_id') in staff_id:
            pass
        else:
            staff_list.append(staff.get('name'))

    for shangol in shangol_data:
        if shangol.get('id') in shangol_id:
            pass
        else:
            shangol_list.append({
                'shangol_id': shangol.get('id'),
                'shangol_name': shangol.get('name'),
                'number': post_douyin.find({'shangol_id': shangol.get('id')}).count()
            })
    #         'tags_one': {'$exists': False}
    response = {
        'error': 0,
        'reason': '数据返回。',
        'data': {
            'staff_list': staff_list,
            'shangol_list': shangol_list
        }
    }
    return JsonResponse(response)


