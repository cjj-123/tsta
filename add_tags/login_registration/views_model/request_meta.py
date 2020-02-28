
class RequestMeta:
    def __init__(self):
        pass

    def request_get(self, request_meta):
        if request_meta.lower() == 'GET'.lower():
            return True
        else:
            return False

    def request_post(self, request_meta):
        if request_meta.lower() == 'POST'.lower():
            return True
        else:
            return False
