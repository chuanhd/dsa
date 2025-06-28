import pytest

from problems.strings_all_unique_char import all_unique_characters, all_unique_characters_sorted, all_unique_characters_bit_manipulation

def test_all_unique_characters():
    assert all_unique_characters("abcdefg") == True
    assert all_unique_characters("abcdeaf") == False
    assert all_unique_characters("") == True
    assert all_unique_characters("a") == True
    assert all_unique_characters("ab") == True
    assert all_unique_characters("aa") == False
    assert all_unique_characters("abcABC") == True
    assert all_unique_characters("abcabc") == False
    assert all_unique_characters("1234567890") == True
    assert all_unique_characters("12345678901234567890") == False

def test_all_unique_characters_sorted():
    assert all_unique_characters_sorted("abcdefg") == True
    assert all_unique_characters_sorted("abcdeaf") == False
    assert all_unique_characters_sorted("") == True
    assert all_unique_characters_sorted("a") == True
    assert all_unique_characters_sorted("ab") == True
    assert all_unique_characters_sorted("aa") == False
    assert all_unique_characters_sorted("abcABC") == True
    assert all_unique_characters_sorted("abcabc") == False
    assert all_unique_characters_sorted("1234567890") == True
    assert all_unique_characters_sorted("12345678901234567890") == False

def test_all_unique_characters_bit_manipulation():
    assert all_unique_characters_bit_manipulation("abcdefg") == True
    assert all_unique_characters_bit_manipulation("abcdeaf") == False
    assert all_unique_characters_bit_manipulation("") == True
    assert all_unique_characters_bit_manipulation("a") == True
    assert all_unique_characters_bit_manipulation("ab") == True
    assert all_unique_characters_bit_manipulation("aa") == False
    assert all_unique_characters_bit_manipulation("abcabc") == False