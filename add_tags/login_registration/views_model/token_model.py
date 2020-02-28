import jwt
from add_tags.settings import SALT


class TokenModel:
    def __init__(self):
        pass

    def get_username(self, token):
        user_name = jwt.decode(token.encode(), SALT).get('username')
        return user_name

    def get_timeout(self, token):
        timeout = jwt.decode(token.encode(), SALT).get('exp')
        return timeout

    def set_timeout(self):
        pass