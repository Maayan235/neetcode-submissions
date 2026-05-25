class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        curr = self.head 
        i = 0 
        while curr != None:
            if i == index:
                return curr[0]
            i+=1
            curr = curr[1]
        return -1
        
    def insertHead(self, val: int) -> None:
        tmp = self.head
        new_head = [val, tmp]
        self.head = new_head
        

    def insertTail(self, val: int) -> None:
        new_tail = [val, None]
        if self.head is None:
            self.head = new_tail
            return
        
        curr = self.head
        while curr[1] != None:
            curr = curr[1]
        curr[1] = new_tail

        

    def remove(self, index: int) -> bool:
        curr = self.head
        pre = None
        i = 0 
        while curr != None:
            if i == index:
                if pre is None:
                    self.head = curr[1]
                else:
                    pre[1] = curr[1]
                return True
            pre = curr
            curr = curr[1]
            i+=1
        return False

    def getValues(self) -> List[int]:
        L = list()
        curr = self.head
        while curr != None:
            L.append(curr[0])
            curr = curr[1]
        return L

