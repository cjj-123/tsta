from add_tags.settings import staff


class TagsInfo:
    def __init__(self):
        pass

    # 获取用户添加的标签信息
    def get_tags(self, username):
        """
        :param username: 用户名
        :return:
        """
        data = {}
        user_info = staff.find_one({'name': username})
        # 获取用户添加的所有标签数量
        tags_all = user_info.get('count')
        if tags_all:
            data['tags_all'] = tags_all
        else:
            # 用户尚未添加标签
            data['tags_all'] = 0
            data['tags_past'] = 0
            data['tags_new'] = 0
            return data
        # 获取用户已结算标签数量
        tags_past = user_info.get('tags_past')
        if tags_past:
            data['tags_past'] = tags_past
        else:
            data['tags_past'] = 0
        # 获取用户新添加标签数量
        tags_new = user_info.get('tags_new')
        if tags_new:
            data['tags_new'] = tags_new
        else:
            data['tags_new'] = 0
        return data
