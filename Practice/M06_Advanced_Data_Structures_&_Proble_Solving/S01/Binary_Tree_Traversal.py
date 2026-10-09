class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#Tree structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#Tree Traversal techniques  94,
'''
1)DFS
    1)pre order(root ->left ->right)
    2)in order(left -> root ->right)
    3)post order(left ->right ->root)
2)BFS(level order)
'''
def pre_order(root):
    if root:
        print(root.data,end = "->")
        pre_order(root.left)
        pre_order(root.right)
pre_order(root)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data,end = "->" )
        in_order(root.right)
print("\n In-order-Traversal")
in_order(root)
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data,end = "->")
print("\n post-order")
post_order(root)

#94. Binary Tree Inorder Traversal
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def in_order(root):
            if root:
                in_order(root.left)
                res.append(root.val)
                in_order(root.right)
        in_order(root)
        return res
from collections import deque
def Level_Order(root):
    if root is None:
        return 
    d = deque([root])
    while d:
        node = d.popleft()
        print(node.data,end = "->")
        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)

print("\n Level Order Traversal")
Level_Order(root)