class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    """20.LL:Constructor"""
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    """21.LL:Print List"""
    # we write our own method - cause there is no same built-in method
    def print_ll_fully(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    """22.LL:Append"""
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    """25.LL:Pop"""
    # is more complicated cause tail pointer needs to shift in the opposite direction,
    # when all nodes pointers point only to the straight direction
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    """26.LL:Prepend - add item to the beginning of LL"""
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    """27.LL:Pop First"""
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp

    """28.LL:Get"""
    def get(self, index):
        if index < 0 or index >= self.length: # index should not be out of range
            return None
        temp = self.head
        for _ in range(index): # _ instead of i cause we're not going to use i in for loop
            temp = temp.next
        return temp.value

    """29.LL:Set"""
    def set_value(self, index, value): # set is a keyword in Python
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    """30.LL:Insert"""
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False # cause if successful we return True
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    """31.LL:Remove"""
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None # cause if successful we return node
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    """32.LL:Reverse"""
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_ll = LinkedList(1)
print(my_ll.head.value) # 1
my_ll.append(2)
my_ll.print_ll_fully()
print(my_ll.pop()) # 2 items - returns 2 node
print(my_ll.pop()) # 1 item - returns 1 node
print(my_ll.pop()) # 0 items - returns None

print(my_ll.prepend(3)) # 3
print(my_ll.prepend(2)) # 2 3
print(my_ll.prepend(1)) # 1 2 3
print(my_ll.pop_first) # 2 3
print(my_ll.get(2)) # 3
print(my_ll.set_value(1, 4)) # 2 4
print(my_ll.insert(1,1)) # 2 1 4
print(my_ll.remove(2)) # 2 4
print(my_ll.reverse()) # 4 2
