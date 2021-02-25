# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:38:26 2021
 
@author: omarm
"""
 
 
#                  A  
#              /   |  \  
#            B     C    D
#           / \    /   / \
#          E   F  N   G   H
#             / \      \
#            I   J       K
 
# Creating the TreeNode class
class TreeNode:
    def __init__(self, value):
        self.children = []
        self.value = value
 
    def BreadthFirstSearch(self):
        visited = []
        currentTreeNode = self
        queue = [currentTreeNode]
        while len(queue) > 0:
            currentTreeNode = queue.pop(0) # POP the value out of the queue
            visited.append(currentTreeNode.value) #PUSH the value into the result array
            for child in currentTreeNode.children: #PUSH the Children into the queue
                queue.append(child)
        return visited
 
    def DepthFirstSearch(self, visited = []):
        visited.append(self.value)
        for child in self.children:
            child.DepthFirstSearch(visited)
        return visited
 
 
# Creating the TreeNodes    
A = TreeNode("A")
B = TreeNode("B") 
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")
G = TreeNode("G")
N = TreeNode("N")
I = TreeNode("I")
J = TreeNode("J")
K = TreeNode("K")
H = TreeNode("H")
 
# Assigning the children
A.children = [B,C,D]
B.children = [E,F]
C.children = [N]
D.children = [G,H]
E.children = []
F.children = [I,J]
I.children = []
J.children = []
N.children = []
G.children = [K]
H.children = []
 
 
#                  A  
#              /   |  \  
#            B     C    D
#           / \    /   / \
#          E   F  N   G   H
#             / \      \
#            I   J       K
 
print("DFS \n")  
ArrayTreeNodes = A.DepthFirstSearch(visited = [])
print(ArrayTreeNodes)
 
print("BFS\n")
ArrayTreeNodes = A.BreadthFirstSearch()
print(ArrayTreeNodes)
