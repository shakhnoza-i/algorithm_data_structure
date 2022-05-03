"""FIFO
Implementation
 - add to the end and remove from the beginning: - both O(1) in LinkedList
                                               : - first O(1) and another O(n) in list
add to the end - last - Enqueue
remove from the beginning - first - Dequeue
"""


"""47.Queue: Constructor"""
class Node: # same as LinkedList
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    """48.Queue: Enqueue"""
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else: 
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    """49.Queue: Dequeue"""
    def dequeue(self, value):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp


my_queue = Queue(8)
my_queue.print_queue() # 8
my_queue.enqueue(11) # 8 11
my_queue.enqueue(12) # 8 11 12
my_queue.dequeue() # 11 12
