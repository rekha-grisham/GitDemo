import pytest


def test_firstProgram():
    print("Good Morning")

@pytest.mark.smoketest
def test_Credit():
    a=4
    b=2
    assert a+2 == 6

def test_crossBrowser(crossBrowser):#the crossBrowser method is defined in the conftest.py file as a fixture
    #with params. Each time the test is run with different params
    print("hello")
    print(crossBrowser)

def test_crossBrowser2(browser):
    print("hello1")
    print("develop branch changes")

    print(browser)
    print(browser[1])