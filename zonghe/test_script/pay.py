

@pytest.fixture(params=DataRead.read_yaml(r"test_data\pay.yaml"))
def pay(request):
    return request.param

def pay():
