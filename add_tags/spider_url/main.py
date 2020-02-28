from spider_url.sittings import post_douyin, video
from spider_url.spider_urls import spider_url
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

video_infos = video.find()
count = 0
for video_info in video_infos:
    sharing_url = video_info.get('sharing_url')
    video_url = spider_url.get(url=sharing_url, headers=headers)
    if video_url:
        post_douyin.insert({
            'video_id': video_info.get('video_id'),
            'sharing_url': sharing_url,
            'shangol_id': video_info.get('shangol_id'),
            'video_date': video_info.get('video_date'),
            'video_url': video_url
        })
    else:
        post_douyin.insert({
            'video_id': video_info.get('video_id'),
            'sharing_url': sharing_url,
            'shangol_id': video_info.get('shangol_id'),
            'video_date': video_info.get('video_date')
        })