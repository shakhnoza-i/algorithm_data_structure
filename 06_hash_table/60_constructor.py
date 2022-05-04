""" In hash table you should always have a prime number of addresses.
"""


class HashTable:
    def __init__(self, size = 7): # create HT with size - 7
        self.data_map = [None] * size # all items contains None

    # ord(letter) - gets the ASCII number for each letter
    # 23 - prime number
    def __hash(self, key): # O(1)
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash # return address from 0 to 6

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", + val)

    """61.HT:Set - O(1)"""
    def set_item(self, key, value): 
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    """62.HT:Get - O(n), but usually is O(1)"""
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])): # runs inside items
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    # Key lookup is O(1) but not value.
    """63.HT:Keys"""
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys



my_ht = HashTable()
my_ht.print_table()
my_ht.set_item('bolts', 1400)
my_ht.set_item('nails', 1800)
my_ht.set_item('wrenchs', 200)

print(my_ht.get_item('nails')) # 1800
print(my_ht.keys()) # ['bolts', 'nails', 'wrenchs']
