from __future__ import annotations

class LLNode:
    def __iter__(self):
        head = self
        yield head
        while head.next is not None:
            yield (head := head.next)
        return StopIteration("Cannot iterate further")

    @property
    def length(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length


class SLLNode(LLNode):
    def __init__(self, value, next_item: SLLNode = None) -> None:
        self.value = value
        self.next = next_item

    def insert(self, new_node: SLLNode, n: int):
        if n == 1:
            new_node.next = self
        elif self.length < n:
            return IndexError("Attempted to insert the Node too far.")
        else:
            to_insert_after = self
            while n-1:
                n -= 1
                to_insert_after = to_insert_after.next
            
            new_node.next = to_insert_after.next
            to_insert_after.next = new_node
        return new_node
    
    def delete(self, n: int):
        if self.length < n:
            return IndexError("Attempted to delete a non-existant node")
        prev = None
        to_delete = self
        for _ in range(n-1):
            prev = to_delete
            to_delete = to_delete.next

        if prev is not None:
           prev.next = to_delete.next
        del to_delete

class DLLNode(LLNode):
    def __init__(self, value, prev: DLLNode = None, next: DLLNode = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next        

    def link_next(self, next_node: DLLNode):
        self.next = next_node
        next_node.prev = self

    def insert(self, node: DLLNode, n: int):
        if n == 1:
            node.next = self
            self.prev = node
        elif self.length < n:
            return IndexError("Attempted to insert the Node too far.")
        else:
            to_insert_after = self
            while n-1:
                n -= 1
                to_insert_after = to_insert_after.next
            
            to_insert_after.prev = node
            node.next = to_insert_after.next
            to_insert_after.next = node
            node.prev = to_insert_after
        return node

    def delete(self, n: int):
        if self.length < n:
            return IndexError("Attempted to delete a non-existant node")

        delete_node = self
        for _ in range(n-1):
            delete_node = delete_node.next

        if delete_node.prev is None:
            delete_node.next.prev = None
        else:
            if delete_node.next is not None:
                delete_node.next.prev = delete_node.prev
            delete_node.prev.next = delete_node.next
        del delete_node
