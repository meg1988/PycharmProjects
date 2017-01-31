import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo4():

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_demo1_methodA(self):
        result = self.abc.sumOfNumbers(10,8)
        assert result == 38
        print("Running demo 1 Method A")

    def test_demo2_methodB(self):
        print("Running demo 1Method B")