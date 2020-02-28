from django.test import TestCase
import requests
import re
# Create your tests here.
url = 'https://www.iesdouyin.com/share/video/6682866724485844236/?region=CN&mid=6682948356731341575&u_code=g4eggb9a&titleType=title'
headers = { 'authority': 'www.iesdouyin.com',
            'method': 'GET',
            'path': '/share/video/6682866724485844236/?region=CN&mid=6682948356731341575&u_code=g4eggb9a&titleType=title',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'tt_webid=6783094612946699789; _ba=BA0.2-20200118-5199e-P2vjUtZzEjxpzTZcOUP3; _ga=GA1.2.1879781412.1579312290; _gid=GA1.2.1445868285.1579312290',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
           }
text = requests.get(url=url,headers=headers).text
print(text)
par = 'playAddr: "(.+)"'

url = re.findall(par, text)
print(url)
