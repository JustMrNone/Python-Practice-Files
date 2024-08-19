from plates import is_valid


def test_starting_letters():
    assert is_valid("CS50") == True
    assert is_valid("cs50") == True
    assert is_valid("50CS") == False


def test_first_number_used():
    assert is_valid("CS05") == False
    assert is_valid("CS15") == True


def test_max():
    assert is_valid("OUTATIME") == False
    assert is_valid("O") == False
    assert is_valid("YA") == True
    assert is_valid("12") == False
    assert is_valid("123456") == False
    assert is_valid("1234567") == False


def test_numbers_in_the_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_punctuation_marks():
    assert is_valid("??????") == False
    assert is_valid("AAA.22") == False
    assert is_valid("AAAA_A") == False
    assert is_valid("AAA AA") == False
    assert is_valid("A?AAA1") == False
    assert is_valid("aaaaa1") == True
