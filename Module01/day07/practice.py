import time
from collections import deque


# 2. LIST VS DICT LOOKUP TIMING
print("--- 2. List vs Dict ---")
lst = [f"ACC_{i}" for i in range(100000)]
dct = {f"ACC_{i}": i for i in range(100000)}
target = "ACC_99999"

t0 = time.time()
_ = target in lst
print(f"List lookup: {time.time() - t0:.6f} sec")

t0 = time.time()
_ = target in dct
print(f"Dict lookup: {time.time() - t0:.6f} sec")


# 3. BUILD A STACK (LIFO)
print("\n--- 3. Stack Reverse ---")
class Stack:
    def __init__(self): self.items = []
    def push(self, val): self.items.append(val)
    def pop(self): return self.items.pop()

s = Stack()
for name in ["Abebe", "Chaltu", "Dawit"]: 
    s.push(name)
print("Reversed:", [s.pop() for _ in range(3)])


# 4. BUILD A QUEUE (FIFO)
print("\n--- 4. Bank Line Queue ---")
q = deque()
for customer in ["Alem", "Bekele", "Chala"]: 
    q.append(customer)
while q: 
    print(f"Served: {q.popleft()}")


# 5. SINGLY LINKED LIST
print("\n--- 5. Linked List Chain ---")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_all(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

ll = LinkedList()

ll.print_all()
