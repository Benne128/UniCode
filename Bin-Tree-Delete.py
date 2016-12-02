"""A simple binary tree with the delete node or child function implemented where it takes a node and searches left and right for children if there is none then the node is deleted"""
#include <iostream>
class Node:
 def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        parent=parent

class BinTreeNode(tree, Node):

    def child_count(self):
#Counts all of the child nodes
        count = 0
        if tree.left:
            count += 1
        if tree.right:
            count += 1
        return count
        
#finds all values in the tree using right and left functions to search the tree correctly for all of its values 
def tree_find(tree,target):
    r=tree
    while r != None:
        if r.value == target:
            return ("item has been found"),r.value
        elif r.value > target:
            r=r.left
    else:
        r=r.right
    return None
#the function for deleting the node itself if it has no child node 
def node_delete(self,value):
    if children_count == 0:
        if parent:
            if tree.left is target:
                tree.left=None
        else:
            tree.right=None
        del target
        
#function for inserting the branches to the tree using the left and right functions to make sure that the nodes have children        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
#the tree nodes  
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
  print (tree_find(t,2))
