import pytest

from dsa.stack import Stack

def test_stack_push():
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    assert stack.peek() == 15
    assert len(stack) == 3

def test_stack_pop():
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    assert stack.pop() == 15
    assert stack.peek() == 10
    assert len(stack) == 2
    assert stack.pop() == 10
    assert stack.peek() == 5
    assert len(stack) == 1
    assert stack.pop() == 5
    assert len(stack) == 0
    with pytest.raises(IndexError):
        stack.pop()

def test_stack_peek():
    stack = Stack()
    stack.push(5)
    stack.push(10)
    assert stack.peek() == 10
    stack.pop()
    assert stack.peek() == 5
    stack.pop()
    with pytest.raises(IndexError):
        stack.peek()

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(5)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True 