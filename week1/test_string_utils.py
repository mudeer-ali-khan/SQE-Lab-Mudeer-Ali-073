import pytest
from string_utils import *


# =========================
# count_vowels
# =========================

def test_count_vowels_basic():
    assert count_vowels("hello") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_case_insensitive():
    assert count_vowels("HELLO") == 2


# =========================
# reverse_string
# =========================

def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single():
    assert reverse_string("a") == "a"

def test_reverse_string_palindrome():
    assert reverse_string("madam") == "madam"


# =========================
# is_palindrome
# =========================

def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_is_palindrome_sentence():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False


# =========================
# word_count
# =========================

def test_word_count_basic():
    assert word_count("hello world") == 2

def test_word_count_spaces():
    assert word_count("   spaces   ") == 1

def test_word_count_single_word():
    assert word_count("Python") == 1


# =========================
# capitalise_words
# =========================

def test_capitalise_words_basic():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_single():
    assert capitalise_words("python") == "Python"

def test_capitalise_words_mixed_case():
    assert capitalise_words("pyTHon proGRAM") == "Python Program"


# =========================
# remove_duplicates
# =========================

def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_single():
    assert remove_duplicates("a") == "a"

def test_remove_duplicates_long():
    assert remove_duplicates("aaaabbbbccccdddd") == "abcd"


# =========================
# EDGE CASES + TYPE ERROR
# =========================

def test_none_inputs_raise_type_error():
    with pytest.raises(TypeError):
        count_vowels(None)

    with pytest.raises(TypeError):
        reverse_string(None)

    with pytest.raises(TypeError):
        is_palindrome(None)

    with pytest.raises(TypeError):
        word_count(None)

    with pytest.raises(TypeError):
        capitalise_words(None)

    with pytest.raises(TypeError):
        remove_duplicates(None)


def test_word_count_edge_empty():
    assert word_count("") == 0
