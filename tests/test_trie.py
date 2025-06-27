import pytest

from dsa.trie import Trie

def test_trie_insert_and_search():
    trie = Trie()
    words = ["hello", "world", "trie", "test"]
    
    for word in words:
        trie.insert(word)
    
    for word in words:
        assert trie.search(word) == True
    
    assert trie.search("hell") == False
    assert trie.search("worlds") == False
    assert trie.search("testa") == False

def test_trie_prefix_search():
    trie = Trie()
    words = ["hello", "hell", "heaven", "heavy"]
    
    for word in words:
        trie.insert(word)
    
    assert trie.starts_with("he") == True
    assert trie.starts_with("hell") == True
    assert trie.starts_with("hello") == True
    assert trie.starts_with("h") == True
    assert trie.starts_with("hi") == False
    assert trie.starts_with("heavenly") == False

def test_trie_empty():
    trie = Trie()
    
    assert trie.search("anything") == False
    assert trie.starts_with("any") == False
    
    trie.insert("a")
    assert trie.search("a") == True
    assert trie.starts_with("a") == True
    
    trie.insert("ab")
    assert trie.search("ab") == True
    assert trie.starts_with("a") == True
    assert trie.starts_with("ab") == True

def test_trie_edge_cases():
    trie = Trie()
    
    # Insert empty string
    trie.insert("")
    assert trie.search("") == True
    assert trie.starts_with("") == True
    
    # Search for empty string
    assert trie.search("") == True
    
    # Search for non-inserted word
    assert trie.search("nonexistent") == False
    
    # Starts with empty string should always return True
    assert trie.starts_with("") == True
    
    # Insert single character
    trie.insert("x")
    assert trie.search("x") == True
    assert trie.starts_with("x") == True

def test_trie_case_sensitivity():
    trie = Trie()
    
    # Insert words with different cases
    trie.insert("Hello")
    trie.insert("hello")
    
    # Search for both cases
    assert trie.search("Hello") == True
    assert trie.search("hello") == True
    assert trie.search("HELLO") == False
    
    # Starts with should be case-sensitive
    assert trie.starts_with("He") == True
    assert trie.starts_with("he") == True
    assert trie.starts_with("HE") == False

def test_trie_long_words():
    trie = Trie()
    
    # Insert long words
    long_word1 = "a" * 1000
    long_word2 = "b" * 1000
    
    trie.insert(long_word1)
    trie.insert(long_word2)
    
    assert trie.search(long_word1) == True
    assert trie.search(long_word2) == True
    assert trie.search("a" * 999) == False
    assert trie.search("b" * 999) == False
    
    assert trie.starts_with("a" * 500) == True
    assert trie.starts_with("b" * 500) == True
    assert trie.starts_with("c" * 500) == False

def test_trie_unicode():
    trie = Trie()
    
    # Insert unicode words
    unicode_word1 = "こんにちは"  # Japanese for "Hello"
    unicode_word2 = "你好"        # Chinese for "Hello"
    
    trie.insert(unicode_word1)
    trie.insert(unicode_word2)
    
    assert trie.search(unicode_word1) == True
    assert trie.search(unicode_word2) == True
    assert trie.search("こんにちは世界") == False  # "Hello World" in Japanese
    
    assert trie.starts_with("こん") == True
    assert trie.starts_with("你") == True
    assert trie.starts_with("世界") == False  # "World" in Chinese

def test_trie_delete():
    trie = Trie()
    words = ["apple", "app", "apricot"]
    
    for word in words:
        trie.insert(word)
    
    # Delete a word
    trie.delete("app")
    assert trie.search("app") == False
    assert trie.search("apple") == True
    assert trie.search("apricot") == True
    
    # Delete another word
    trie.delete("apple")
    assert trie.search("apple") == False
    assert trie.search("apricot") == True
    
    # Delete a word that doesn't exist
    trie.delete("banana")
    assert trie.search("apricot") == True