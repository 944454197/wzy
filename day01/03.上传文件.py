import requests

# 接口路径
# url = "http://192.168.150.70:8089/carRental/file/upLoadFile.action"
# # 本地存在的文件
# file = "C:/Users/94445/Desktop/Mercedes.png"
# # rb二进制只读的方式打开
# with open(file, mode='rb') as f:
#     # {'name': file-tuple}
#     # {'filename', fileobj,'content_type'}
#     cs = {"filename": (file, f, "image/png")}
#     r = requests.post(url, files=cs)
#     print(r.text)


# http://192.168.150.70:8089/carRental/file/upLoadFile.action
# 租车系统上传图片
url = "http://localhost:8080/carRental/file/uploadFile.action"
file = "C:/Users/94445/Desktop/Mercedes.png"
with open(file, mode='rb') as f:
    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)
    uploadPath = r.json()['data']['src']

# 添加车,使用刚上传的图片
url = "http://localhost:8080/carRental/car/addCar.action"
cs = {
    "carnumber": "陕BB487V", "cartype": "东风本田", "color": "黑色",
    "carimg": uploadPath, "description": "2020年新车",
    "price": 200000, "rentprice": 1000, "deposit":500, "isrenting": 0
}
head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
r = requests.post(url, data=cs, headers=head)
print(r.text)