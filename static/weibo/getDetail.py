import os
import sys
import requests

import json

data = ''


class API:
    serviceURL = "https://m.weibo.cn/api/"
    config = serviceURL + "config"
    channelList = serviceURL + "config/list"
    contain = serviceURL + "container/getIndex?containerid="
    lbs = serviceURL + "lbs/near?"
    detail = serviceURL + "detail/"
    hotflow = serviceURL + "../comments/hotflow?id=%s&mid=%s"


headers = {
    "Host": "m.weibo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
}

cookies = {
    "M_WEIBOCN_PARAMS": "luicode=10000011&lfid=102803&uicode=10000011&fid=102803",
    "WEIBOCN_FROM": "1110006030"
}

with open(os.path.join(sys.path[0], '../hot.json'), 'r+') as f:
    data = f.read()

data = json.loads(data)

data = data['data']['cards']

for i in data:
    mid = i['mblog']['mid']
    print(mid)
    try:
        response = requests.get(API.hotflow.replace('%s',mid), headers=headers)
        print(API.hotflow.replace('%s',mid))
        try:
            assert response.status_code == 200,'IP被微博拉入黑名单，请稍后再试'
            with open(os.path.join(sys.path[0],mid+'.json'),'w+') as j:
                j.write(response.text)
        except Exception as e:
            print(e)
            sys.exit(-1)
    except requests.ConnectionError as e:
        print("连接失败", e.args)