#Any pytest file should start with test_ or end with test_
import pytest


#we have to write any code as function in pytest
#pytest stand we call test methods. Always start with test
#any code should be wrapped in method only

#command line execution is by suing the command py.test with -v and -s options . -v mena sdetails of the execution
#-s means the print statements output to be displayed
# to execute any specific test case just give the name
#-k to execute all test cases with a specific wor like (all credit card test cases).
#-m(marked test cases) is to execute test cases which are marked as smoke or regression with pytest mark
#to mark(tag) a test case use @pytest.mark.smoketest
#example py.test -m smoketest -v -s


@pytest.mark.smoketest
def test_firstPgm():
    print("Hello")


def test_firstPgmCredit():
    msg = "Credit"
    print(msg)
    assert msg == "Credit"


