'''
pytest命名约束：
1、文件用test_开头
2、类用Test开头
3、函数或方法用test_开头
'''
import requests
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = [
    {"mobilephone": '18012345678', "pwd": '123456'},
    {"mobilephone": 'asd', "pwd": '123456'},
    {"mobilephone": '13100859154', "pwd": '12345'},
    {"mobilephone": '13100859154', "pwd": '123456'}

]

def test_register_001():
    r = requests.get(url, cs[0])
    rjson = r.json();
    assert rjson['status'] ==0
    print("注册成功的脚本")



def test_register_002():
    r = requests.get(url, cs[1])
    rjson = r.json();
    assert rjson['status'] == 0
    print("手机号码格式不正确")


def test_register_003():
    r = requests.get(url, cs[2])
    rjson = r.json();
    assert rjson['status'] == 0
    print("密码不足6位")

def test_register_004():
    r = requests.get(url, cs[3])
    rjson = r.json();
    assert rjson['status'] == 0
    print("注册成功")
