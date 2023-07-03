class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            print("List is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.is_empty():
            print("List is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def display(self):
        if self.is_empty():
            print("List is empty.")
        else:
            current = self.head
            while current:
                print(current.value, end=" <-> ")
                current = current.next
            print("None")


dll = DoublyLinkedList()

dll.insert_at_end(5)
dll.insert_at_end(10)
dll.insert_at_end(15)

dll.display()  # Output: 5 <-> 10 <-> 15 <-> None

dll.delete_at_beginning()
dll.display()  # Output: 10 <-> 15 <-> None

dll.insert_at_beginning(2)
dll.display()  # Output: 2 <-> 10 <-> 15 <-> None

dll.delete_at_end()
dll.display()  # Output: 2 <-> 10 <-> None
