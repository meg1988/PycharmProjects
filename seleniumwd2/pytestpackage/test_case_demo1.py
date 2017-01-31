import pytest

@pytest.fixture()
def setUp():
    print("this will execute once before every method.demo 1")

def test_demo1_methodA(setUp):
    print("Running demo 1 Method A")

def test_demo2_methodB(setUp):
    print("Running demo 1Method B")