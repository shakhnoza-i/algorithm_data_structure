"""
The idea behind merged sort is this if you have two sorted lists and 
combine them into a new sorted list.
Stages: 
- first break this list in half and break it in half again until we have one item
- we can take two of the items and create a new list that's sorted
- take two new lists and merge them into new sorted list and again and again
"""

"""
85. Merge function 
Merge is a helper function. It doesn't do all of what is required for merge sort.
It just does a portion of it. Next video we write this helper function.
"""


"""86. Merge code"""
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1    
    return combined    

print(merge([1,2,7,8], [3,4,5,6]))


"""
87. Merge sort - breaks list in half
We use recursion: 
1) breaks lists in half
2) base case: when len(my_list) is 1
3) Uses merge() to put lists together
"""


"""88. Merge sort - code"""
def merge_sort(my_list):
    if len(my_list) == 1: # divide until 1 item in list only
        return  my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid] # include 0 and until mid(not included)
    right = my_list[mid:] # include mid and until the last
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([3,1,4,2]))


"""
88. Merge sort - BigO

Space comlpexity - O(n) - cause the number of items being stored in memory 
have been doubled (new list created)

Time comlpexity:
- breaking in half until 1 one item - O(log(n))
- merge it together - O(n)
In result we get - O(n * log(n))
O(n * log(n)) - is most efficient when you going to sort multiple types of data
"""

