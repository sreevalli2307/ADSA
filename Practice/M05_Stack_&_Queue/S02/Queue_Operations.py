#enque,deque,peek
#queue implementation using ront and rare pointers
class Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q =[None] * self.size
    def enqueue(self,val):
        if self.rear == self.size-1 :
            return "Queue is full"
        if self.front == -1:
            self.front = 0
        self.rear+=1
        self.q[self.rear] = val
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        self.front+=1
        val = self.q[self.front]
        return val
    def display(self):
        if self.front == -1:
            print( "Queue is empty")
            return 
        for i in range(self.front,self.rear+1):
            print(self.q[i],end = "->")
        print()
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.dequeue()
q.display()
#Queue implementation using linked list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,val):
        new_node = Node(val)
        if self.front is None:
            self.front = self.rare = new_node
            return 
        self.rare.next = new_node
        self.rare = new_node
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        val = self.front.data
        self.front = self.front.next 
        if self.front is None:
            self.rare = None
        return val
    def display(self):
        temp = self.front
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()
q1 = Queue_LL()
q1.enqueue(100)
q1.enqueue(200)
q1.enqueue(300)
q1.display()
q1.dequeue()
q1.dequeue()
q1.display()