import pytest

from dsa.linked_list import LinkedList

def test_linked_list_insert():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.head.value == 15
    assert ll.head.next.value == 10
    assert ll.head.next.next.value == 5

def test_linked_list_search():
    ll = LinkedList()
    ll.insert(5) # List: 5
    ll.insert(10) # List: 10 -> 5
    ll.insert(15) # List: 15 -> 10 -> 5
    assert ll.search(10).value == 10
    assert ll.search(20) is None
    assert ll.search(5).value == 5

def test_linked_list_delete():
    ll = LinkedList()
    ll.insert(5) # List: 5
    ll.insert(10) # List: 10 -> 5
    ll.insert(15) # List: 15 -> 10 -> 5
    ll.delete(10) # List: 15 -> 5
    assert ll.head.value == 15
    assert ll.head.next.value == 5
    assert ll.search(10) is None
    ll.delete(5)
    assert ll.head.value == 15
    assert ll.search(5) is None
    ll.delete(15)
    assert ll.head is None
    assert ll.search(15) is None