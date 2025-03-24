import requests

# 定义请求的URL
# id = 64是领取签到3天的奖励，id=65是10天
url = "https://weapp.top-dianjingfeng.com/weapp/mine/addScoreSignCycle?id=65&openId=ohff45HMkOK9VF8JYEDMYW5rQTK8&memberId=f229b93702f24603ab31163c08b39f7f&userId=2067093"

# 定义请求头
headers = {
    "openId": "ohff45HMkOK9VF8JYEDMYW5rQTK8",
    "content-type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "Referer": "https://servicewechat.com/wx6faafa56d8e3e9ce/83/page-frame.html",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Host": "weapp.top-dianjingfeng.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.56(0x18003839) NetType/4G Language/zh_CN"
}


try:
    # 发送GET请求
    response = requests.get(url, headers=headers)
    data = response.json()
    code = data.get('code')
    # 打印响应状态码和响应体
    print(code)

except Exception as e:
    # 捕获并打印请求过程中可能出现的异常
    print(f"An error occurred: {e}")