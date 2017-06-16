#coding:utf-8
from urllib import request
import json

# 随机使用一个百度云用户号
uk = 1700262137
start = 0
limit = 60
url = 'http://pan.baidu.com/pcloud/feed/getsharelist?category=0&auth_type=1&request_location=share_home&start=%d&limit=%d&query_uk=%d' % (start, limit, uk)
ref = 'http://pan.baidu.com/share/home?uk=%d' % uk
x_ip = '123.123.123.77'  # 此IP地址可以随机生成

header = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': ref,
    'X-Forwarded-For': x_ip
}
req = request.Request(url, headers=header)
page = request.urlopen(req).read()

share_json = json.loads(page)
if (share_json['errno'] != 0):
    print('errno:%d' % share_json['errno'])
    exit()
else:
    #只要能显示出来，说明能正常爬取了，只为实验提取一部分
    share_count = share_json["total_count"]
    print("分享数量:", share_json["total_count"])
    if share_count >= limit:
        share_count = 60
    print("运行数量:", share_count)
    for i in range(share_count):
        print("----------%d---------" % (start + i + 1))
        print("分享名称:", share_json["records"][i]["title"])
        print("分享链接:", "http://pan.baidu.com/s/"+share_json["records"][i]["shorturl"])

