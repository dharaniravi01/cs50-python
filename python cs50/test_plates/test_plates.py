from plates import is_valid


def test_len():
    assert is_valid("w") == False

def test_punc():
    assert is_valid("WA!02") == False

def test_firstletter():
    assert is_valid("12328") == False

def test_zero():
    assert is_valid("WWA012") == False

def test_num():
    assert is_valid("WW123A") == False

def test_alp():
    assert is_valid("WWW222") == True


