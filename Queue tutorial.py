from collections import deque
from time import sleep
import threading
class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

que = Queue()

def place_order(order_list):
    for element in order_list:
        que.enqueue(element)
        sleep(0.5)
    return que

def serve_order():
    while not que.is_empty():
        print("Serving: ", que.dequeue())
        sleep(2)

"""
orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target = place_order, args = (orders,))
t2 = threading.Thread(target = serve_order)

t1.start()
t2.start()

t1.join()
t2.join()
"""

q = Queue()
for i in range(10):
    q.enqueue(i)
print(q.dequeue())

#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md ---- Exercise 2      
        