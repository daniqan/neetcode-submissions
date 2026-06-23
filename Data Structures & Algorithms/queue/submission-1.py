class Node:
    def __init__(self, val: int):
        self.val = val              # store value
        self.prev = None            # pointer to previous node
        self.next = None            # pointer to next node

class Deque:
    def __init__(self):
        self.head = None            # pointer to first node
        self.tail = None            # pointer to last node
        self.size = 0               # track number of elements

    def isEmpty(self) -> bool:
        # True if no elements in deque
        return self.size == 0

    def append(self, value: int) -> None:
        # Add node at the end (tail)
        new_node = Node(value)
        if self.tail:               # if deque not empty
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:                       # if empty, head and tail are same
            self.head = self.tail = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        # Add node at the beginning (head)
        new_node = Node(value)
        if self.head:               # if deque not empty
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:                       # if empty
            self.head = self.tail = new_node
        self.size += 1

    def pop(self) -> int:
        # Remove node from end (tail)
        if self.isEmpty():
            return -1
        val = self.tail.val
        if self.head == self.tail:  # only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return val

    def popleft(self) -> int:
        # Remove node from beginning (head)
        if self.isEmpty():
            return -1
        val = self.head.val
        if self.head == self.tail:  # only one element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return val