class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("already empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("empty stack")

    def size(self):
        return len(self.items)


stack = Stack()

print(stack.is_empty())  # Output: True

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.size())  # Output: 3

print(stack.peek())  # Output: 30

print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20

print(stack.size())  # Output: 1

print(stack.pop())  # Output: 10

print(stack.pop())  # Output: already empty
