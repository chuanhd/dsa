import pytest

from dsa.queue import Queue

def test_queue_enqueue():
  queue = Queue()
  queue.enqueue(5)
  queue.enqueue(10)
  queue.enqueue(15)
  assert queue.peek() == 5
  assert len(queue) == 3

def test_queue_dequeue():
  queue = Queue()
  queue.enqueue(5)
  queue.enqueue(10)
  queue.enqueue(15)
  assert queue.dequeue() == 5
  assert queue.peek() == 10
  assert len(queue) == 2
  assert queue.dequeue() == 10
  assert queue.peek() == 15
  assert len(queue) == 1
  assert queue.dequeue() == 15
  assert len(queue) == 0
  with pytest.raises(IndexError):
      queue.dequeue()

def test_queue_peek():
  queue = Queue()
  queue.enqueue(5)
  queue.enqueue(10)
  assert queue.peek() == 5
  queue.dequeue()
  assert queue.peek() == 10
  queue.dequeue()
  with pytest.raises(IndexError):
      queue.peek()

def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(5)
    assert queue.is_empty() is False
    queue.dequeue()
    assert queue.is_empty() is True

def test_queue_length():
  queue = Queue()
  assert len(queue) == 0
  queue.enqueue(5)
  assert len(queue) == 1
  queue.enqueue(10)
  assert len(queue) == 2
  queue.dequeue()
  assert len(queue) == 1
  queue.dequeue()
  assert len(queue) == 0

def test_queue_multiple_operations():
  queue = Queue()
  queue.enqueue(1)
  queue.enqueue(2)
  assert queue.peek() == 1
  assert len(queue) == 2
  assert queue.dequeue() == 1
  assert queue.peek() == 2
  queue.enqueue(3)
  assert len(queue) == 2
  assert queue.dequeue() == 2
  assert queue.peek() == 3
  assert len(queue) == 1
  assert queue.dequeue() == 3
  assert len(queue) == 0
  with pytest.raises(IndexError):
      queue.peek()
      queue.dequeue()