
from qs import deserialize

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_deserialize():
    assert deserialize() == 5