#20,232
class Circular_Queue:
    def __init__(self,size):
        self.size = size 
        self.front = -1 
        self.rear = -1
        self.q = [None]*self.size

    def enqueue(self,val):
        #Queue is full or not
        if self.front == (self.rear+1)%self.size:
            return "Queue is Full"
        if self.front == -1:
            self.front ==0
        self.rare = (self.rear+1)%self.size
        self.q[self.rear] = val 
    def dequeue(self):
        if self.front == -1:
            return "Queue is Empty"

        val = self.q[self.front];
        self.q[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return val
