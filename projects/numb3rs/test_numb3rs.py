from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("01.01.01.01") == True
    assert validate("255.256.256.256") == False

def test_validate_range():
    assert validate("255.255.255.2555") == False

def test_validate_no_input():
    assert validate("") == False

def test_validate_string():
    assert validate("Cat") == False
    assert validate("Dog") == False

