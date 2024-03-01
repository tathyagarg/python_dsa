from __future__ import annotations

class SLLNode:
    def __init__(self, value, next_item = None) -> None:
        self.value = value
        self.next_item = next_item

    def __iter__(self):
        head = self
        yield head
        while head.next_item is not None:
            yield (head := head.next_item)
        return StopIteration("Cannot iterate further")

    @property
    def length(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length

    def insert(self, new_node: SLLNode, n: int):
        if n == 1:
            new_node.next_item = self
        elif self.length < n:
            return IndexError("Attempted to insert the Node too far.")
        else:
            to_insert_after = self
            while n-1:
                n -= 1
                to_insert_after = to_insert_after.next_item
            
            new_node.next_item = to_insert_after.next_item
            to_insert_after.next_item = new_node
        return new_node
    
    def delete(self, n: int):
        if self.length < n:
            return IndexError("Attempted to delete a non-existant node")
        prev = None
        to_delete = self
        while n-1:
            n -= 1
            prev = to_delete
            to_delete = to_delete.next_item

        if prev is not None:
           prev.next_item = to_delete.next_item
        del to_delete

        
