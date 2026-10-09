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

'''
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
