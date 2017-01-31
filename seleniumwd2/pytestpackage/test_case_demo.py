import pytest
from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.abc = SomeClassToTest(10)

    def test_demo1_methodA(self):
        result = self.abc.sumOfNumbers(10,8)
        assert result == 20
        print("Running demo 1 Method A")

    def test_demo2_methodB(self):
        print("Running demo 1Method B")