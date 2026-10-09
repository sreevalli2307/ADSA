'''
Height: the longest path between the nodes
2)Ways
1)Edges
2)Nodes
height = 1+max(height(left),height(right))




'''
def Height(root):
    if root is None:
        return -1
    left = Height(root.left)
    right = Height(root.right)
    return 1 + max(left, right)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(0)
root.left = Node(20)
print("height is", Height(root))
