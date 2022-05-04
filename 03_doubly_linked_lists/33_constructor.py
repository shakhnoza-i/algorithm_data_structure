class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

node = {
        'value': 7, 
        'next': None, 
        'prev': None
        }

class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll_fully(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    """34.DLL:Append"""
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True
    
    """35.DLL:Pop"""
    # O(1) - simplier cause we have pointer to previous value and we 
    # don't need to iterate over the entire list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp.value

    """36.DLL:Prepend"""
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True

    """37.DLL:Pop First"""
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head = None
            temp.next = None
        self.length -=1
        return temp.value

    """38.DLL:Get"""
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index): 
                temp = temp.next
        else: 
            for _ in range(self.length - 1, index, -1): 
                temp = temp.prev
        return temp.value

    """39.DLL:Set"""
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    """40.DLL:Insert"""
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False # cause if successful we return True
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    """
    41.DLL:Remove"""
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None # cause if successful we return node
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp.value



my_dll = DoublyLinkedList(7)
print(my_dll.print_dll_fully()) # 7
print(my_dll.append(2)) # 7 2
print(my_dll.pop()) # 7
print(my_dll.prepend(1)) # 1 7
print(my_dll.prepend(3)) # 3 1 7
print(my_dll.pop_first()) # 1 7
print(my_dll.get(0))  # 1
print(my_dll.set_value(0, 3))  # 3 7
print(my_dll.insert(0, 6)) # 6 3 7
print(my_dll.insert(1, 1)) # 6 1 3 7
print(my_dll.remove(2)) # 6 1 7
