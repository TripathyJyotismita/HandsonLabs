'''
3. Binary Search TreeALGORITHMIC THINKING RECURSION TREE   Easy
A three-node binary tree.Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.

Write a function that, efficiently with respect to time used, checks if a given binary search tree contains a given value.

For example, for the following tree:

n1 (Value: 1, Left: null, Right: null)
n2 (Value: 2, Left: n1, Right: n3)
n3 (Value: 3, Left: null, Right: null)
Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
'''
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    #print('xxx', root, value)
    #for root in root:
    #    print('root', root)
    pass

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

#print(contains(n2, 3))


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        print(data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def vfind(self, value):
        print('in find')
        print('v', value)
        print('self.data', self.data)
        if value < self.data:
            if self.left is None:
                print('not found', value)
            print(self.left.vfind(value))
        if value > self.data:
            if self.right is None:
                print ('not found', value)
            print(self.right.vfind(value))



    def printTree(self):
        print(self.data)



root = Node(10)
root.insert(6)
root.insert(7)
root.insert(11)
root.vfind(11)
root.printTree()

