class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        counter = 0
        while temp:
            if counter == index:
                return temp.val
            temp = temp.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        counter = 0
        while temp and counter < index - 1:
            temp = temp.next
            counter += 1
        if not temp:
            return
        node = ListNode(val)
        node.next = temp.next
        temp.next = node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        counter = 0
        while temp and counter < index - 1:
            temp = temp.next
            counter += 1
        if not temp or not temp.next:
            return
        temp.next = temp.next.next
