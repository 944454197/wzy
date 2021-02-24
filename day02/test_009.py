'''
fixture 嵌套
'''
import random
import pytest
import requests


# # 生成用户名
# @pytest.fixture()
# def get_username():
#     return "admin" + str(random.randint(1, 1000))
#
#
# # 生成密码
# @pytest.fixture()
# def get_pwd():
#     return random.randint(100000, 9999999999)
#
# @pytest.fixture()
# def get_login_data(get_username, get_pwd):
#     return {"username": get_username, "pwd": get_pwd}
#
# # 测试用例
# def test_login(get_login_data):
#     print("测试登录功能，登录的数据为：{get_login_data}")

# 练习：用fixture+requests，优化金融项目注册接口的脚本
url = "http://jy001:8081/futureloan/mvc/api/member/register"

@pytest.fixture()
def get_mobilephone():
    return "phonenumber" + random.randint(10000000000, 99999999999)

@pytest.fixture()
def get_pwd():
    return "密码" + random.randint(100000,999999999999999999)

@pytest.fixture()
def get_mobilephone1():
    return "phonenumber" + str(random.randint(10000000000, 99999999999))

@pytest.fixture()
def get_pwd1():
    return "密码" + random.randint(100000, 999999999999999999)

@pytest.fixture()
def get_mobilephone2():
    return "phonenumber" + random.randint(10000000000, 99999999999)

@pytest.fixture()
def get_pwd2():
    return "密码" + random.randint(0,99999)

@pytest.fixture()
def get_login_data():
    return {"mobilephone": get_mobilephone, "pwd":get_pwd}

@pytest.fixture()
def get_login_data1():
    return {"mobilephone": get_mobilephone1, "pwd":get_pwd1}

@pytest.fixture()
def get_login_data2():
    return {"mobilephone": get_mobilephone2, "pwd":get_pwd2}

def test_login(get_login_data):
    r = requests.get(url, get_login_data)
    rjson = r.json()
    assert rjson['status'] == 0
    print("注册成功")

def test_login1(get_login_data1):
    r = requests.get(url, get_login_data1)
    rjson = r.json()
    assert rjson['status'] == 0
    print("手机号码格式不正确")

def test_login2(get_login_data2):
    r = requests.get(url, get_login_data2)
    rjson = r.json()
    assert rjson['status'] == 0
    print("密码不足6位")
