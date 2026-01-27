import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample:

    def test_profileData(self,dataLoad):
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])
        print(dataLoad[0])# chenges for develop branch 3