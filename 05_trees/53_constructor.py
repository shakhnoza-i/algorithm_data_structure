""" 
52.BST: BigO
O(log(n)) - lookup(), insert(), remove(), retrieve()

add data to a data structure very quickly, but retrieval speed 
isn't very important - LinkedList is better - O(1), while BST - O(log(n))

Insert in BST - Omega (best case) and Theta (average case) are both (log n). 
However, worst case is O(n) and Big O measures worst case.
"""

"""53.BST: Constructor"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self): # init empty BST
        self.root = None

    """55.BST: Insert-Into"""
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    """56.BST: Contains"""
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    """57.BST: Minimum Value"""
    def minimum_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    """97.BFS: Code - traverse and print all values in bst"""
    def bfs(self):
        current_node = self.root
        results = []
        queue = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results # list is in the same order as tree itself - 
                       # row by row from top to bottom

    """99.DFS preorder: Code"""
    def dfs_preorder(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    """101.DFS postorder: Code"""
    def dfs_postorder(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    """103.DFS inorder: Code"""
    def dfs_inorder(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


my_tree = BinarySearchTree()

print(my_tree.root) # None
my_tree.insert(8)
my_tree.insert(5)
my_tree.insert(13)
print(my_tree.root.value) # 8
print(my_tree.root.left.value) # 5
print(my_tree.root.right.value) # 13
my_tree.insert(7)
my_tree.insert(2)
my_tree.insert(10)
my_tree.insert(15)
print(my_tree.contains(7)) # True
print(my_tree.contains(14)) # False
print(my_tree.minimum_value(my_tree.root)) # 2
print(my_tree.minimum_value(my_tree.root.right)) # 10
print(my_tree.bfs())
