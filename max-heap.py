import heapq

max_heap = []

# Insert elements into the max heap with negated values
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -10)

# Remove and return the largest element from the max heap
largest = heapq.heappop(max_heap)
print(largest)  # Output: 10

# Access the largest element without removing it
largest = -max_heap[0]
print(largest)  # Output: 8
for i in max_heap:
    print(-1 * i)
