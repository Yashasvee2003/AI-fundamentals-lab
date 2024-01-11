import heapq

# Create an empty list to represent the heap
heap = []

# Push elements (tuples) onto the heap
heapq.heappush(heap, (5, "A"))
heapq.heappush(heap, (3, "B"))
heapq.heappush(heap, (7, "C"))
heapq.heappush(heap, (2, "D"))

# Pop elements from the heap in ascending order of the first element of each tuple
while heap:
    value, data = heapq.heappop(heap)
    print(f"Value: {value}, Data: {data}")