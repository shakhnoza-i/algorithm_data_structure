"""LIFO
Exaample of using: back_button, previous
The ways to implement stack: 
- using list (simpliest way):
    - to add and remove from the same end(the end) - O(1)
    - to add and remove from another end(beginning) - O(n)
- using linked list:
    - to add from tail - O(1), for remove - O(n) - Bottom
    - to add and remove from the head - O(1) - Top
    In stack we only need to add(push) and remove(pop) from the top
"""


"""43.Stack: Constructor"""
class Node: # same as LinkedList
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node # we only work with the top and now we don't need bottom (tail)
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    """44.Stack: Push"""
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length +=1
        return True

    """45.Stack: Pop"""
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp


my_stack = Stack(3)
my_stack.print_stack()
my_stack.push(2) # 2 3
my_stack.push(5) # 5 2 3
my_stack.pop() # 2 3

