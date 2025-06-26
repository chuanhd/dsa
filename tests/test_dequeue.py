import pytest

from dsa.dequeue import Deque

def test_deque_append():
    deque = Deque()
    deque.append(5)
    deque.append(10)
    deque.append(15)
    assert deque.peek() == 5
    assert len(deque) == 3

def test_deque_append_left():
    deque = Deque()
    deque.append_left(5)
    deque.append_left(10)
    deque.append_left(15)
    assert deque.peek() == 15
    assert len(deque) == 3

def test_deque_pop():
    deque = Deque()
    deque.append(5)
    deque.append(10)
    deque.append(15)
    assert deque.pop() == 15
    assert deque.peek() == 5
    assert len(deque) == 2
    assert deque.pop() == 10
    assert deque.peek() == 5
    assert len(deque) == 1
    assert deque.pop() == 5
    assert len(deque) == 0
    with pytest.raises(IndexError):
        deque.pop()

def test_deque_pop_left():
    deque = Deque()
    deque.append(5)
    deque.append(10)
    deque.append(15)
    assert deque.pop_left() == 5
    assert deque.peek() == 10
    assert len(deque) == 2
    assert deque.pop_left() == 10
    assert deque.peek() == 15
    assert len(deque) == 1
    assert deque.pop_left() == 15
    assert len(deque) == 0
    with pytest.raises(IndexError):
        deque.pop_left()  

def test_deque_peek():
    deque = Deque()
    deque.append(5) # [5]
    deque.append(10) # [5, 10]
    assert deque.peek() == 5
    deque.pop() # [5]
    assert deque.peek() == 5
    deque.pop()
    with pytest.raises(IndexError):
        deque.peek()

def test_deque_is_empty():
    deque = Deque()
    assert deque.is_empty() is True
    deque.append(5)
    assert deque.is_empty() is False
    deque.pop()
    assert deque.is_empty() is True

def test_deque_length():
    deque = Deque()
    assert len(deque) == 0
    deque.append(5)
    assert len(deque) == 1
    deque.append(10)
    assert len(deque) == 2
    deque.pop()
    assert len(deque) == 1
    deque.pop()
    assert len(deque) == 0

def test_deque_multiple_operations():
    deque = Deque()
    deque.append(1)
    deque.append(2)
    deque.append_left(3)
    assert deque.peek() == 3
    assert len(deque) == 3
    assert deque.pop_left() == 3
    assert deque.peek() == 1
    assert len(deque) == 2
    assert deque.pop() == 2
    assert deque.peek() == 1
    assert len(deque) == 1
    assert deque.pop_left() == 1
    assert len(deque) == 0
    with pytest.raises(IndexError):
        deque.pop()
    with pytest.raises(IndexError):
        deque.pop_left()  