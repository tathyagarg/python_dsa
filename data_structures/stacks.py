from .arrays import Array

class Stack:
    def __init__(self, size: int = 127) -> None:
        self.items = Array(int, size=size)
        self.curr_stack_size = 0
        self.max_size = size

    def push(self, item: int):
        if self.curr_stack_size == self.max_size:
            return OverflowError("Stack overflow")
        self.items[self.curr_stack_size] = item
        self.curr_stack_size += 1
    
    def pop(self) -> int:
        result = self.items.pop()
        self.curr_stack_size -= 1
        return result

    @property    
    def top(self) -> int:
        if self.curr_stack_size == 0:
            return None
        return self.items[self.curr_stack_size-1]
    
    @property
    def size(self) -> int:
        return self.curr_stack_size

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def is_full(self) -> bool:
        return self.size == self.max_size



