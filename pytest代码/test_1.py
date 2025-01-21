import pytest
@pytest.mark.parametrize("param1", [1, 2, 3])
@pytest.mark.parametrize("param2", [4, 5, 6])
def test_multiple_parameters(param1, param2):
    print(param1 + param2)
    assert param1 + param2
