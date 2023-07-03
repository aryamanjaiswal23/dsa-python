from collections import deque

dq = deque()
print(dq)  # Output: deque([])

dq.append(1)  # Add to the right end
dq.append(2)
dq.appendleft(0)  # Add to the left end
print(dq)  # Output: deque([0, 1, 2])

item = dq.pop()  # Remove and return the rightmost element
print(item)  # Output: 2
item = dq.popleft()  # Remove and return the leftmost element
print(item)  # Output: 0
print(dq)  # Output: deque([1])

item = dq[-1]  # Access the rightmost element without removing it
print(item)  # Output: 1
item = dq[0]  # Access the leftmost element without removing it
print(item)  # Output: 1

size = len(dq)
print(size)  # Output: 1

dq.reverse()
print(dq)  # Output: deque([1])

dq.clear()
print(dq)  # Output: deque([])

is_empty = len(dq) == 0
print(is_empty)  # Output: True
