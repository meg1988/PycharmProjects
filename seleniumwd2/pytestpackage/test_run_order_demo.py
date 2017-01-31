import pytest


@pytest.mark.run(after='test_run_order_methodC')
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("running method A")

@pytest.mark.run(order=5)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("running method B")

@pytest.mark.run(order=6)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("running method C")

@pytest.mark.run(order=3)
def test_run_order_methodD(oneTimeSetUp, setUp):
    print("running method D")

@pytest.mark.run(order=2)
def test_run_order_methodE(oneTimeSetUp, setUp):
    print("running method E")

@pytest.mark.run(order=1)
def test_run_order_methodF(oneTimeSetUp, setUp):
    print("running method F")

