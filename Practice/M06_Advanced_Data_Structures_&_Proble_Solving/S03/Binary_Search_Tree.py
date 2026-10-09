'''
Binary search tree:Bst is the  tree which follow 2 rules:
1) the value is smallest when compare with the curr val insert in left sub-tree
2)the value is larger when compare with the curr val insert in right sub-tree
Repreesentation:
                    50
                   /  \
                  40   70
                 /  \   / \
                20  45  60 80
Left-sub-tree:20,45,40<root node(50)
Right sub-tree:60,70,80>root node(50)


class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
root = Node(50)
root.left = Node(40)
root.left.left = Node(20)
root.left.right = Node(45)
root.right= Node(70)
root.right.left =Node(60)
root.right.right = Node(80)

Operations:
1)Search 
2)Insert
3)Delete
4)Validation
5)Traversal

Algorithm:
1>check with root node (if not available return --> None)
2> if key == node.data:
    --> return True
3> if key > node.data:
-->search in right sub-tree
4> -->Search in left sub-tree

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(node, key):
    # Step 1: Check if root node is None
    if node is None:
        return None
    
    # Step 2: If key matches node.data
    if key == node.data:
        return True
    
    # Step 3: If key is greater, search in right subtree
    if key > node.data:
        return search(node.right, key)
    
    # Step 4: Otherwise, search in left subtree
    return search(node.left, key)


# Example usage:
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print(search(root, 40))  # True
print(search(root, 25))  # None

#700. Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        curr = root
        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
