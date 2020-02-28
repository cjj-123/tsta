import pymongo
connect = pymongo.MongoClient(host='localhost', port=27017)
db = connect.shangjing
staff = db.staff


class ClauseModel:

    def __init__(self):
        pass

    def agree_clause(self, user_name):
        user_info = staff.find_one({'name': user_name})
        if user_info:
            staff.update({'name': user_name},{'$set':{'clause': 'ok'}})
            return 'ok'
        else:
            return 'error'

    def disagree_clause(self):
        return 'remove'
