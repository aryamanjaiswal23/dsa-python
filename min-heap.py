import heapq

heap = []
# min heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1

# Access the smallest element without removing it
smallest = heap[0]
print(smallest)  # Output: 3

for i in heap:
    print(i)  # Output: 3 4 8 10
