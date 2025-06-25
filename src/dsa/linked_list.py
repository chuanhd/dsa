class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # **insert**: Inserts a new node with the given value at the beginning of the linked list.
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    # Example: If the linked list is currently 3 -> 5, and we insert 2, it becomes 2 -> 3 -> 5.
    def insert(self, value):
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # # **insert**: Inserts a new node with the given value after the specified node in the linked list.
    # # Time Complexity: O(1)
    # # Space Complexity: O(1)
    # # Example: If the linked list is currently 3 -> 5, and we insert 4 after the node with value 3, it becomes 3 -> 4 -> 5.
    # # If the node is None, it will insert at the end of the list.
    # # If the node is the last node, it will insert at the end of the list
    # def insert_after(self, node, value):
    #     newNode = ListNode(value)
    #     if not node is None:
    #         newNode.next = node.next
    #     node.next = newNode

    # **search**: Searches for a node with the specified value in the linked list.
    # Time Complexity: O(n), where n is the number of nodes in the linked list
    # Space Complexity: O(1)
    # Example: If the linked list is 3 -> 5 -> 7 and we search for 5, it returns the node with value 5.
    # If the value is not found, it returns None.
    # If the linked list is empty, it returns None.
    # If the value is found, it returns the node with that value.
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    # **delete**: Deletes the first occurrence of a node with the specified value from the linked list.
    # Time Complexity: O(n), where n is the number of nodes in the linked list
    # Space Complexity: O(1)
    # Example: If the linked list is 3 -> 5 -> 7 and we delete 5, it becomes 3 -> 7.
    # If the value is not found, the linked list remains unchanged.
    # If the linked list is empty, it remains unchanged.
    def delete(self, value):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next


