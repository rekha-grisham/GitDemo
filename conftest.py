import pytest

@pytest.fixture(scope="class")
def setup():
    print("setup steps")
    yield#here the execution is handed to the actual test case--test_world
    print("teardown steps")

@pytest.fixture
def dataLoad():
    print("User data profile is being created")
    return["Rekha", "Halapeti", "rekhaniki9875@gmial.com"]

@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param

@pytest.fixture(params=[("Chrome","Rekha", "Halapeti"), ("Firefox","Rekha"), ("IE","R")])
def browser(request):
    return request.param