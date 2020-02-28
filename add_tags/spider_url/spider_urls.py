import time
import requests
import re
par = 'playAddr: "(.+)"'


class SpiderUrl:

    def __init__(self):
        pass

    def get(self, url, headers=None, params=None, *args, **kwargs):
        while True:
            try:
                response = requests.get(url=url, headers=headers, params=params, timeout=5).text
                url = re.findall(par, response)
                print(url)
                time.sleep(2)
                if url:
                    return url[0]
                else:
                    return ''
            except Exception as error:
                print(error)
                time.sleep(2)

    def post(self):
        pass
spider_url = SpiderUrl()