import pytest 

@pytest.mark.smoke
def test_sample_one():
    print("Hai")
def test_sample1():
    a=5
    b=10
    assert a<b

@pytest.mark.regression
def test_sample3():
    a="arun"
    b="arun"
    assert a.__eq__(b)