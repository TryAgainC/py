import requests

# 定义请求的URL
url = "https://weapp.top-dianjingfeng.com/weapp/mine/addScoreSign?memberId=f229b93702f24603ab31163c08b39f7f"

# 定义请求头
headers = {
    "openId": "ohff45HMkOK9VF8JYEDMYW5rQTK8",
    "content-type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "Referer": "https://servicewechat.com/wx6faafa56d8e3e9ce/73/page-frame.html",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Host": "weapp.top-dianjingfeng.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.56(0x1800382e) NetType/WIFI Language/zh_CN"
}

body = ''

# 发送GET请求
response = requests.get(url, headers=headers,data=body)

data = response.json()
print(data.get('code'))