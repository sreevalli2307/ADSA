class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self, value):
        self.q.append(value)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.q[0]
        else:
            return "Queue is empty"
    def is_empty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    
        
# Create queue
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
