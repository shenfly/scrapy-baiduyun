# scrapy-baiduyun
百度云盘，python3爬取技术分析

get_sharehome.py 爬取共享文件
1.必须带上header
2.header中必须有Referer
3.header中带上 X-Forwarded-For，可以防止爬取 -55错误，而且不需要用换代理。

