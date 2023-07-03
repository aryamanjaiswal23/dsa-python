class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_begin(self, val):
        newn = Node(val)
        if self.is_empty():
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn

    def insert_at_end(self, val):
        newn = Node(val)
        if self.is_empty():
            self.head = newn
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newn
            newn.next = None

    def delete_at_begin(self):
        if self.is_empty():
            print("nothing to delete")
        else:
            self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            print("nothing to delete")
        elif self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            while self.head:
                print(self.head.data, end="->")
                self.head = self.head.next
            print("none")


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third
llist.insert_at_begin(0)
llist.delete_at_end()
llist.display()  # Output: 0->1->2->none
