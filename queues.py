class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)


q = Queue()
print(q.is_empty())  # Output: True
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.peek())  # Output: 2
print(q.size())  # Output: 3
q.dequeue()
q.dequeue()
print(q.size())  # Output: 1
print(q.peek())  # Output: 4
