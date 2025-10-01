import heapq

class CustomPriorityQueue:
   def __init__(self):
       self.heap = []

   def push(self, priority, value):
       heapq.heappush(self.heap, (priority, value)) 

   def pop(self):
       return heapq.heappop(self.heap)

   def peek(self):
       return self.heap[0] if self.heap else None

   def is_empty(self):
       return not self.heap


pq = CustomPriorityQueue()
pq.push(2, "Task B")
pq.push(1, "Task A")
pq.push(3, "Task C")

print(pq.pop())
print(pq.peek())


import heapq

# Creating a list and converting it into a heap
numbers = [5, 1, 8, 3, 7]
heapq.heapify(numbers)
print("Heapified list:", numbers)

# Adding elements to the heap
heapq.heappush(numbers, 2)
print("After pushing 2:", numbers)

# Removing the smallest element
smallest = heapq.heappop(numbers)
print("Popped smallest element:", smallest)
print("Heap after pop:", numbers)