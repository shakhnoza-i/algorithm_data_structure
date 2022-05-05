"""
In insertion sort we always start from the second item and compare it to
item before it. And swap them if second item is less
"""

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

print(insertion_sort([4,2,6,5,1,3]))

"""O(n^2) in worst case, O(n) in almost sorted list - and this is True for only insertion sort"""
"""All three of these sort the list in place. That means that they do not 
create additional copies of the list. That means it the space complexity is O(1)"""
