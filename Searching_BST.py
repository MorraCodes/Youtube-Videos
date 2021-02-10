"""
Created on Mon 18:37:57 2021

#            10
#           /  \
#         6     15
#        /       \
#       2         20
#                   
#       

@author: Omar (MorraCodes)
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

                     
    def find(self, value):
        currentNode = self # Object
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    
    def Print_Tree(self): # Inorder , Source for this print function https://cppsecrets.com/users/323979711510410511697115104535364103109971051084699111109/Python-Program-to-print-all-the-elements-in-Binary-Search-tree.php
        if self.left:
            self.left.Print_Tree()
        print(self.value, end=' ') 
        if self.right:
            self.right.Print_Tree()
                
    

# Creating the Nodes   ---- No connections between them  
Node1 = BinarySearchTree(10)
Node2 = BinarySearchTree(6)
Node3 = BinarySearchTree(15)
Node4 = BinarySearchTree(2)
Node5 = BinarySearchTree(20)

             
# Asigning the left and the right attributes
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node3.right = Node5



Node1.Print_Tree()

print()
print(Node1.find(15))















