#enque,deque,peek
#queue implementation using ront and rare pointers
class Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q =[None] * self.size
    def enqueue(self,val):
        if size.rare == self.size-1 :
            return "Queue is full"
        self.rear+=1
        self.q[self.rear] = val
    def dequeue(self):
        
