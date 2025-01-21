import pytest


@pytest.fixture(scope="module")
def fix():
    print("用例执行前")

    yield

    print("用例执行后")



