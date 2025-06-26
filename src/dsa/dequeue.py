class Deque:
  def __init__(self):
    self.items = []

  def append(self, item):
    """Append an item to the end of the deque."""
    self.items.append(item)

  def append_left(self, item):
    """Append an item to the front of the deque."""
    self.items.insert(0, item)

  def pop(self):
    """Pop an item from the end of the deque and return it."""
    if self.is_empty():
      raise IndexError("pop from empty deque")
    return self.items.pop()
  
  def pop_left(self):
    """Pop an item from the front of the deque and return it."""
    if self.is_empty():
      raise IndexError("pop_left from empty deque")
    return self.items.pop(0)
  
  def peek(self):
    """Return the front item of the deque without removing it."""
    if self.is_empty():
      raise IndexError("peek from empty deque")
    return self.items[0]
  
  def is_empty(self):
    """Check if the deque is empty."""
    return len(self.items) == 0 
  
  def __len__(self):
    """Return the number of items in the deque."""
    return len(self.items)