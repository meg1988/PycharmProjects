import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo 2 setup")
    yield
    print("Running demo 2 teardown")


def test_demo2_methodA(setUp):
    print("Running demo 2 Method A")

def test_demo2_methodB(setUp):
    print("Running demo 2 Method B")