from mystery_word import *

a = WordGameController()


def test_clean_input_basic():
    assert a.clean_input("easy") == "EASY"

def test_clean_input_numbers():
    assert a.clean_input("easy32082093849") == \
    "EASY"

def test_clean_input_whitespace():
    assert a.clean_input(" easy    ") == "EASY"





def test_clean_input():
    assert a.clean_input("easy") == "EASY"
