import pytest
import requests

cs = [
    # 密码长度为5
    {"data": {"mobilephone": 1801234567, "pwd": "12345"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码长度超过18
    {"data": {"mobilephone": 1801234567, "pwd": "12345678901234567890"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码为空
    {"data": {"mobilephone": 1801234567, "pwd": ""},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
    # 手机号码格式不正确
    {"data": {"mobilephone": 180123456, "pwd": "123456"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}]

@pytest.fixture(params=cs)
def register_data(request):
    return request.param
def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r
def test_register(register_data):
    print(f"测试数据：{register_data['data']}")
    print(f"预期结果：{register_data['expect']}")
    r = register(register_data['data'])
    print(f"实际结果:{r.text}")
    assert r.json()['status'] == register_data['expect']['status']
    assert r.json()['code'] == register_data['expect']['code']
    assert r.json()['msg'] == register_data['expect']['msg']