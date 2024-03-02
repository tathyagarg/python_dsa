from .linked_lists import SLLNode

class Queue:
    def __init__(self) -> None:
        self.head: SLLNode = None
        self.tail: SLLNode = None

    def enqueue(self, value: int):
        if self.is_empty:
            self.head = SLLNode(value)
            self.tail = self.head
        else:
            self.tail.next = SLLNode(value)
            self.tail = self.tail.next

    def dequeue(self):
        if self.is_empty:
            return IndexError("Tried to dequeue from empty queue")

        item: SLLNode = self.head.value
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return item

    @property
    def front(self):
        return self.head.value
    
    @property
    def rear(self):
        return self.tail.value

    @property
    def size(self) -> int:
        if self.is_empty:
            return 0

        length = 0
        for item in self.head:
            length += 1
        return length

    @property
    def is_empty(self) -> bool:
        return self.head is None    

