'''
接口测试
    使用requests中的get post 方法调用接口，检查返回值是否正确
'''

########################### get请求 不带参数 ########################

import requests
# 获取用户列表
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
# 发送请求
r = requests.get(url)
# 打印响应
print(r.text)
# 检查结果与预期是否相同
assert r.status_code == 200
assert r.reason == "OK"
rjson = r.json()
assert rjson['status'] == 1
assert rjson['code'] == '10001'
assert rjson["msg"] == "获取用户列表成功"
# 响应头
print(r.headers)
########################### get请求 带参数 ########################
# 注册接口，参数拼接在URL后面。 ？ 后面是参数，多个参数使用 & 连接
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=17677899943&pwd=123456"
# 发送get请求
r = requests.get(url)
# 打印响应，文本格式
print(r.text)
rjson = r.json()
assert rjson['status'] == 0
assert rjson['code'] == '20110'
assert rjson["msg"] == "手机号码已被注册"

# 注册接口  使用param传参
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {
    "mobilephone": "17634677782",
    "pwd": "123456",
    "regname": "requests_test"
}
r = requests.get(url, params=cs)
print(r.text)
rjson = r.json()
assert rjson['status'] == 0
assert rjson['code'] == '20110'
assert rjson["msg"] == "手机号码已被注册"

# 查询手机号码归属地的接口，参数 ：tel
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=17391805214"
r = requests.get(url)
print(r.text)
# print(r.json())#报错因为返回的结果不是json格式
assert '陕西电信' in r.text