import requests

# 表单格式的数据：content-type: www-x-form-urlencoded,使用data传参。
# 登录接口
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": 18012345678, "pwd": "123456"}
r = requests.post(url, data=cs)
print(r.text)


# json格式的数据：content-type:application/json,使用json传参。
# 具体使用data还是json传参，要看接口怎么定义的。
# httpbin.org 是一个测试网站，不管发生什么类型的数据，
# 这个接口将发送的请求，封装成json格式的返回
url = "http://www.httpbin.org/post"
cs = {"mobilephone": 18012345678, "pwd": "123456"}
r = requests.post(url, data=cs)
print("data传参", r.text)
r = requests.post(url, json=cs)
print("json传参", r.text)

# 租车系统
url = "http://localhost:8080/carRental/car/addCar.action"
# 接口文档中对接口描述不清晰
# 通过界面操作接口对应的功能，抓包（Fiddler、浏览器的F12）看
cs = {
    "carnumber":"123",
    "cartype":"123",
    "color":"123",
    "carimg":"images/defaultcarimage.jpg/",
    "description":"123",
    "price":123,
    "rentprice":123,
    "deposit":123,
    "isrenting":0
}
# 使用接口添加的车辆，中文字符乱码，但是用节目添加的车辆，不会有乱码
# 分别抓接口的包，与界面的包，对比差异。界面设置了charset=UTF-8，但是自动化未设置导致。
head = {
    "Content-Type"
    "User-Agent"

}

# Fiddler 抓脚本的包，设置代理
# proxy = {
#     "http": ""
#     "https": ""
# }
r = requests.post(url, data=cs)
print(r.text)