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
        tags_all = user_info.get('tags_all')
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

    def update_tags(self, username, number):
        '''
        :param username: 员工昵称
        :param number: 结算标签数量
        :return:
        '''
        user_info = staff.find_one({'name': username})
        tags_new = user_info.get('tags_new')
        if tags_new < number:
            data = {
                'error': 1,
                'reason': '您添加的标签数量不够。'
            }
        elif number < 0:
            data = {
                'error': 1,
                'reason': '结算数量有误。'
            }
            return data
        else:
            if not user_info.get('tags_past'):
                staff.update({'name': username}, {'$set': {'tags_past': 0}})
            # 从新获取个人信息
            user_info = staff.find_one({'name': username})
            staff.update({'name': username}, {'$set': {'tags_past': user_info.get('tags_past') + number}})
            staff.update({'name': username}, {'$set': {'tags_new': user_info.get('tags_new') - number}})
            data = {
                'error': 0,
                'reason': '结算成功'
            }
            return data

    def label_recommendation(self, keyword):
        label_list = ['辟谣', '美女模特', '艺术', '财经', '美食', '音乐', '电视剧', '美妆', '游戏', '电影', '萌宠', '育儿', '动漫', '明星', '运动健身', '读书', '汽车', '正能量', '法律', '情感', '政务', '房产', '三农', '宗教', '搞笑', '社会', '综艺', '股市', '设计', '国际', '摄影', '婚庆', '时尚', '家居', '收藏', '健康', '瘦身', '军事', '数码', '科技', '体育', '科普', '舞蹈', '历史', '校园', '旅游', '星座', '美国', '养生', '个人动态', '朋友聚会', 'party', '分享生活', 'talkshow', '高考', '参加活动', '上学', '骑行', '合作', '上班', '音乐会', '娱乐', '中国', '鞋子', '挑战', '中国美食', '非洲', '旅游', '乐器', '雕刻', '测评', '书本', '陶艺', '竞技类', '体育', '身边的人', '美食', '体育节', '身边的事情', '健身', '路人', '参演作品', '足球', '吃饭', '话题', '合作视频', '见面', '吐槽', '衣服', '商业合作', '街边艺术', '喜爱的明星', '英雄联盟', '国外', '英语', '国外的美食', '花花', '娱乐', '舞蹈', '娱乐八卦', '自拍', '学习的方法', '肉类', '宠物', '考研', '宣传', '美食节日', '家庭', '美食', '家电', '美甲', '日常vlog', '美国', '游戏', '网红', '烹饪', '篮球', '照片', '管弦', '爱情', '男朋友', '现场娱乐', '生活', '生病', '甜品', '电影', '瑜伽', '电影节', '王者荣耀', '看电影', '狗', '科技', '爸爸', '穿搭', '爵士', '红人节', '爱情', '网红店', '热点的新闻', '美妆', '美容', '点评电影', '美术', '演唱会', '舞蹈', '演员', '节日', '滑板', '访谈', '游泳', '酒店', '民族', '音乐', '歌手', '欧洲', '模仿名人', '极限运动', '春节', '文化节', '政治', '排球', '拳击', '护肤', '帽子', '工作', '小品', '导演', '家庭', '婴儿', '婚礼', '妈妈', '大提琴', '圣诞节', '唱K', '哥哥', '咖啡厅美食', '吉他', '吃饭', '南美洲', '化妆', '分享片段', '儿童节', '健身', '作家', '乒乓球', '主食', '中国风', '东南亚', '与他人合拍', '丈夫', '万圣节', 'Jazz', 'dota']
        data = []
        # 以列表的形式返回相应的提示
        for word in label_list:
            if keyword in word:
                data.append(word)
        return data

