# test_calculator.py

import pytest


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(0, 1) == -1
    assert subtract(1, 1) == 0


# 启动命令 pytest pytest代码/demo_pytest.py --html=report.html