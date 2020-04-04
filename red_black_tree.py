# Red-Black Tree (Balanced Binary Search Tree) WIP

import math

class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        
    def __str__(self):
        return f'Value: {self.value:<4}: {self.color}'

    __repr__ = __str__

class Tree:
    def __init__(self, max_height=4):
        self.max_nodes = int(math.pow(2, max_height)) - 1
        self.nodes = [None] * self.max_nodes
        self.total = 0
    
    def idx(x):
        return x - 1

    def parent(self, index):
        return self.get_node(math.ceil(index//2))
    
    def left_child(self, index):
        return self.get_node(index * 2)

    def right_child(self, index):
        return self.get_node(index * 2 + 1)

    def get_node(self, index):
        return self.nodes[index - 1]

    def insert(self, value):
        if self.total == 0:
            self.nodes[0] = Node(value, 'b')
            self.total += 1
            return

        c_idx = 1
        while True:
            current = self.get_node(c_idx)
            assert current.value != value

            if value < current.value:
                c_idx = c_idx * 2   # left child index
                if self.get_node(c_idx):
                    continue
                else:
                    self.nodes[c_idx-1] = Node(value, 'r')
                    self.total += 1
                    return
            elif value > current.value:
                c_idx = c_idx * 2 + 1   # right child index
                if self.get_node(c_idx):
                    continue
                else:
                    self.nodes[c_idx-1] = Node(value, 'r')
                    self.total += 1
                    return

    def print(self):
        for i in range(self.max_nodes):
            print(self.nodes[i])


tree = Tree()

tree.insert(4)
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(1)

tree.print()
