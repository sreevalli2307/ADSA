'''
Double Linked List
Data store nodes 
Node 3 parts  
Algorithm:
1) create Node
2)Insert Node
3) connect btw nodes
4) Traverse


'''
'''
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2 
node2.prev = node1 
node2.next = node3 
node3.prev = node2 
node3.next = node4
node4.prev = node3

def traverse_forward():
    curr = node1
    while curr:
        print(curr.data,end = "<->")
        curr = curr.next 
    print("None")
traverse_forward()
def traverse_backward():
    curr = node4
    while curr:
        print(curr.data,end = "<->")
        curr = curr.prev 
    print("None")
traverse_backward()

#Insertion at the beginning
class Node:
    def __init__(self,data):
        self.data = data 
        self.prev = None
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def insert_pos(node,data):
    if node is None:
        print("Error")
        return
    new_node = Node(data)
    new_node.prev = Node
    new_node.next = node.next
    if node.next:
        node.next.prev = new_node
    node.next = new_node



def insert_end(head, data):
    new_node = Node(data)
    if head is None:   
        return new_node
    curr = head
    while curr.next:   
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head

def traverse(head):
    curr = head 
    while curr:
        print(curr.data,end = "<->")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head,10)
head = insert_begin(head,30)
head = insert_begin(head,50)
print("Insertion at the begin")
traverse(head)
print()
head = None
head = insert_end(head, 50)
head = insert_end(head, 30)
head = insert_end(head, 10)
head = insert_end(head, 100)

print("Insertion at the end:")
traverse(head)

#Insertion at the end
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_end(head, data):
    new_node = Node(data)
    if head is None:   
        return new_node
    curr = head
    while curr.next:   
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head

def traverse(head):
    curr = head
    while curr:
        print(curr.data, end="<->")
        curr = curr.next
    print("None")

# Demo
head = None
head = insert_end(head, 50)
head = insert_end(head, 30)
head = insert_end(head, 10)
head = insert_end(head, 100)

print("Insertion at the end:")
traverse(head)
'''


        