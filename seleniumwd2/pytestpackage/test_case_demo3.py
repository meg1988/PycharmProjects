import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo 3 setup")
    yield
    print("Running demo 3 teardown")


def test_demo3_methodA(setUp):
    print("Running demo 3 Method A")

def test_demo3_methodB(setUp):
    print("Running demo 3 Method B")