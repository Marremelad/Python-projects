from pizza import convert
import pytest

def test_pizza():

    with pytest.raises(SystemExit):
        convert("sicilians.csv")
