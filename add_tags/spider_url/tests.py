# from django.test import TestCase

# Create your tests here.
import requests
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "tt_webid=6783087464901150215; _ba=BA0.2-20200118-5199e-hr7ndvVyK5cnuId6mxvp; _ga=GA1.2.42677137.1579310624; _gid=GA1.2.1766940693.1579484804",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
url = 'https://www.iesdouyin.com/share/video/6758363210350415116/?region=CN&mid=6758351273864563470&u_code=g4eggb9a&titleType=title'
# url = 'https://www.iesdouyin.com/share/video/6751678310494866700/?region=CN&mid=6751657284377578253&u_code=g4eggb9a&titleType=title'
response =  requests.get(url=url, headers=headers).text
par = 'playAddr: "(.+)"'
url = re.findall(par,response)
print(url[0])