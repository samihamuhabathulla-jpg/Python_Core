import pytest_check as check

def test_soft():

    print("Start")

    check.equal(1, 1, "First Assertion")
    print("After First Assertion")

    check.equal(3, 3, "Second Assertion")
    print("After Second Assertion")

    check.equal(5, 5, "Third Assertion")
    print("After Third Assertion")

    print("End")