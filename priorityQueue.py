from queue import PriorityQueue

pq = PriorityQueue()
pq.put((3, 'Task C'))
pq.put((1, 'Task A'))
pq.put((2, 'Task B'))

while not pq.empty():
    priority, item = pq.get()
    print(f"Processing: {item} (Priority: {priority})")