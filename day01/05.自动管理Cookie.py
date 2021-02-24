'''
requests.session 来保持状态。自动管理过程中产生的cookie，
下次请求自动带上上一次的cookie
'''

import requests

# requests.get()
s = requests.session()
print(s.cookies) # RequestsCookieJar
# 通过dict_from_cookiejar 将cookie转成字典
print("登录前的cookies:", requests.utils.dict_from_cookiejar(s.cookies))
# 登录接口
url = "https://www.bagevent.com/user/login"
cs = {
    "account": "2780487875@qq.com",
    "password": "qq2780487875"
}
r = s.post(url, data=cs)
print(r.text)
print("登陆后的cookies",requests.utils.dict_from_cookiejar(s.cookies))

# dashboard接口
r = s.get("https://www.bagevent.com/account/dashboard")
print(r.text)
# assert "<title>百格活动 - 账户总览</title>" in r.text

# 退出登录的接口
r = s.get("https://www.bagevent.com/user/login_out")
print("退出的cookies:", requests.utils.dict_from_cookiejar(s.cookies))