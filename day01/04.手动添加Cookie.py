'''
Cookie 用来识别用户
'''

import requests

# 没有登陆时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上cookie信息
head = {
    "Cookie":'_ga=GA1.2.362341775.1611729517; _gid=GA1.2.1818864636.1611729517; __auc=da03eb1a17742910085f22523e4; MEIQIA_TRACK_ID=1ndozYB2viTeLFN8tyEE51hjzbT; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611729520,1611818289; MEIQIA_VISIT_ID=1ngiiz9EeHI4WnxlciQqgp4lZ8i; __asc=f2ffd88517747db4f734d79c0cc; BAGSESSIONID=f81fbfb2-dceb-400b-ae28-cfeb14df3e7a; JSESSIONID=28E0F7C5BD375A918DD51D71F1934BB3; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611818578'
}
r = requests.get(url, headers=head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

'''
缺点：
1.cookie会失效，失效后需要重新获取
2.登陆后的每个接口，需要带着cookie
'''
