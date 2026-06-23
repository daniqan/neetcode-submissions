# Node class for doubly linked list
class Node:
    def __init__(self, value: int):
        self.value = value          # Store node value
        self.prev = None            # Pointer to previous node
        self.next = None            # Pointer to next node

class Deque:
    def __init__(self):
        self.head = None            # Front of deque
        self.tail = None            # End of deque

    def isEmpty(self) -> bool:
        # Deque is empty if no head node
        return self.head is None

    def append(self, value: int) -> None:
        # Add node to the end in O(1)
        new_node = Node(value)
        if self.tail:               # If deque not empty
            self.tail.next = new_node
            new_node.prev = self.tail
        else:                       # If empty, head = tail = new node
            self.head = new_node
        self.tail = new_node

    def appendleft(self, value: int) -> None:
        # Add node to the front in O(1)
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node

    def pop(self) -> int:
        # Remove node from end in O(1)
        if not self.tail:
            return -1
        val = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val

    def popleft(self) -> int:
        # Remove node from front in O(1)
        if not self.head:
            return -1
        val = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val
        
