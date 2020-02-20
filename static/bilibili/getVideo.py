import os
import sys
import requests

import json

data = ''


class API:
    URL = "https://api.bilibili.com/x/web-interface/ranking/region?rid=%s&day=3&jsonp=jsonp"


headers = {
    "Host": "api.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
    "Referer":"https://www.bilibili.com/"
}

cookies = {
}

for i in '1':
    try:
        response = requests.get(API.URL.replace('%s',str(i)), headers=headers)
        print(API.URL.replace('%s',str(i)))
        try:
            with open(os.path.join(sys.path[0],'ranking'+'.json'),'w+') as j:
                j.write(response.text)
        except Exception as e:
            print(e)
            sys.exit(-1)
    except requests.ConnectionError as e:
        print("连接失败", e.args)