import pymongo


connect = pymongo.MongoClient(host='localhost', port=27017)

new_db = connect.admin_tags
post_douyin = new_db.post_douyin


old_db = connect.shangjing
video = old_db.post_dy

