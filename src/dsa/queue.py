class Queue:
  def __init__(self):
      self.items = []

  def enqueue(self, item):
      """Enqueue an item to the end of the queue."""
      self.items.append(item)

  def dequeue(self):
      """Dequeue an item from the front of the queue and return it."""
      if self.is_empty():
          raise IndexError("dequeue from empty queue")
      return self.items.pop(0)
  
  def peek(self):
      """Return the front item of the queue without removing it."""
      if self.is_empty():
          raise IndexError("peek from empty queue")
      return self.items[0]
  
  def is_empty(self):
      """Check if the queue is empty."""
      return len(self.items) == 0
  
  def __len__(self):
      """Return the number of items in the queue."""
      return len(self.items)
  