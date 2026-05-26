class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        
        
    def append(self, value: int) -> None:
        new_item = Node(value)
        if self.isEmpty():
            new_item.prev = self.head
            self.head.next = new_item
        else:
            curr_last = self.tail.prev
            curr_last.next = new_item
            new_item.prev = curr_last
        new_item.next = self.tail 
        self.tail.prev = new_item

    def appendleft(self, value: int) -> None:
        new_item = Node(value)
        if self.isEmpty():
            new_item.next = self.tail
            self.tail.prev = new_item
        else:
            curr_head = self.head.next 
            curr_head.prev = new_item
            new_item.next = curr_head
        new_item.prev = self.head
        self.head.next = new_item
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        tmp = self.tail.prev
        new_tail = tmp.prev
        new_tail.next = self.tail
        self.tail.prev = new_tail
        return tmp.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        tmp = self.head.next
        new_head = tmp.next
        new_head.prev = self.head
        self.head.next = new_head
        return tmp.val 
        
