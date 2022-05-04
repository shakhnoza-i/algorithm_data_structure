"""
Differences between normal lists and linked lists(LL) that: 
- LL doesn't have indexes
- LL is a contiguous place in memory
- LL have a variable called head and it points to the first node in the LL, and
also have tale point to the last item and then each node points to the next, and 
the last one is just going to point to none
- Nodes are going to be spread out in different places in memory
"""

"""
BigO
add to tail - O(1)
remove from tail - O(n), cause we need to iterate over the entire LL to set tail 
pointer to the last existing element after removing
add to head - O(1)
remove from head - O(1)
add to middle - O(n), cause we need to iterate over the LL to find node after which
we want to set new node
remove from middle - O(n)
"""

"""
Under the hood
What the node is?
Node is the value with next pointer. It's essentially a dictionary
"""

head = {
        "value":11, 
        "next": {
                "value":3, 
                "next": {
                        "value":14, 
                        "next": None
                        }
                }
        }
print(head['next']['next']['value']) # 14
# This will only run with a LL
print(head.next.next.value)
