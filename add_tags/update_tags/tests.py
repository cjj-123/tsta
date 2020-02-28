from django.test import TestCase

# Create your tests here.
# import pymongo
#
# connect = pymongo.MongoClient(host='localhost', port=27017)
# db = connect.test_no
# tests = db.tests
#
# # tests.insert({'name': 'cao'})
# # tests.insert({'name': 'co', 'age': 19})
# # data = tests.find_one({'age': {'$exists': True}})
# # print(data)
# # data = tests.find({'name': 'cao','age': {'$exists': True}})
# # for i in data:
# #     print(i)
# # tests.update({'age': 19},{'$set':{'tags': None}})
#
# data = tests.find()
# for da in data:
#     print(da)

import redis

connect = redis.Redis(host='localhost', port=6379)
name = '曹见f￥平'
connect.set(name, 'name')
connect.delete(name)
print(connect.get(name))