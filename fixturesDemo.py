#fixtures are for setup and teardown methods.
#setup steps are executed first . Used to setup browser and start the browser.
#teardwon is used to delete any data and close teh browser

#when a fixture is used by many test case files,
#we can move the fixture to conftest file  so it will be available for all the files

#we cna declare fixture at class level if we want to use the setup for all the methods

#if we want to run the fixture only at the begining of the class and at the end, not for each test case,
# then we can use the scope = class in the conftest.py file
#fixtures are used for set up and tear down methods
#to call the fixture in before any method, pass the fixture name in the parameter for the method
#data driven and parameterization can be done with return statements in tuple format
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("hello world_1")

    def test_fixtureDemo2(self):
        print("hello world_2")

    def test_fixtureDemo3(setup):
        print("hello world_3")