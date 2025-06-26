class Stack:
  def __init__(self):
      self.items = []

  def push(self, item):
      """Push an item onto the stack."""
      self.items.append(item)

  def pop(self):
      """Pop an item off the stack and return it."""
      if self.is_empty():
          raise IndexError("pop from empty stack")
      return self.items.pop()

  def peek(self):
      """Return the top item of the stack without removing it."""
      if self.is_empty():
          raise IndexError("peek from empty stack")
      return self.items[-1]

  def is_empty(self):
      """Check if the stack is empty."""
      return len(self.items) == 0

  def __len__(self):
      """Return the number of items in the stack."""
      return len(self.items)