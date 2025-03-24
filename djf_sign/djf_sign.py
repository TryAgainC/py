import requests

# 先判断现在签到的是第几天，如果签到第三天，或者第十天，就领累计奖励，第十天跳过签到
headers = {
    "openId": "ohff45HMkOK9VF8JYEDMYW5rQTK8",
    "content-type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "Referer": "https://servicewechat.com/wx6faafa56d8e3e9ce/83/page-frame.html",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Host": "weapp.top-dianjingfeng.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.56(0x18003839) NetType/4G Language/zh_CN"
}
def getsignCount():
    url_getsignCount = "https://weapp.top-dianjingfeng.com/weapp/mine/member/detail?openId=ohff45HMkOK9VF8JYEDMYW5rQTK8&memberId=f229b93702f24603ab31163c08b39f7f&userId=2067093"
    response = requests.get(url_getsignCount, headers=headers)
    data = response.json()
    # 拿出累计签到天数
    signCount = data.get('data').get('signCount')
    return signCount

def getCurrentScore():
    url_getsignCount = "https://weapp.top-dianjingfeng.com/weapp/mine/member/detail?openId=ohff45HMkOK9VF8JYEDMYW5rQTK8&memberId=f229b93702f24603ab31163c08b39f7f&userId=2067093"
    response = requests.get(url_getsignCount, headers=headers)
    data = response.json()
    # 拿出累计签到天数
    currentScore = data.get('data').get('currentScore')
    return currentScore
def getSign():
    url = "https://weapp.top-dianjingfeng.com/weapp/mine/addScoreSign?memberId=f229b93702f24603ab31163c08b39f7f"
    response = requests.get(url, headers=headers)
    data = response.json()
    # 签到成功则是code == 200,签到失败code == 500，code是int类型
    code = data.get('code')
    return code

def getsignReward3():
    url = "https://weapp.top-dianjingfeng.com/weapp/mine/addScoreSignCycle?id=64&openId=ohff45HMkOK9VF8JYEDMYW5rQTK8&memberId=f229b93702f24603ab31163c08b39f7f&userId=2067093"
    response = requests.get(url, headers=headers)
    data = response.json()
    code = data.get('code')
    return code
def getsignReward10():
    url = "https://weapp.top-dianjingfeng.com/weapp/mine/addScoreSignCycle?id=65&openId=ohff45HMkOK9VF8JYEDMYW5rQTK8&memberId=f229b93702f24603ab31163c08b39f7f&userId=2067093"
    response = requests.get(url, headers=headers)
    data = response.json()
    code = data.get('code')
    return code

if __name__ == '__main__':
    before_sign_score = getCurrentScore()
    signCount = getsignCount()
    msg = ''
    if signCount == 3:
        sign_code3 = getSign()
        reward_code3 = getsignReward3()
        if sign_code3 == 200 and reward_code3 == 200:
            msg = '签到成功，获取连签3天奖励'
        else:
            msg = '签到失败'
    elif signCount == 10:
        reward_code10 = getsignReward10()
        if reward_code10 == 200:
            msg = '获取连签10天奖励,今日不签到'
        else:
            msg = '获取连签10天奖励失败'
    else:
        sigon_code = getSign()
        if sigon_code == 200:
            msg = '签到成功'
        else:
            msg = '签到失败'

    after_sign_score = getCurrentScore()
    requests.get(f'https://api.day.app/LzKC6mQqMS3aKiX2RA3MML/电竞蜂/{msg}。之前积分：{before_sign_score}，之后积分：{after_sign_score}')
