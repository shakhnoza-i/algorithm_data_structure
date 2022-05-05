"""
The way Quicksort works is we start with a pivot point that's going to 
be that first item. Then we're going to compare each of the numbers 
after that to this to see if it's greater than or less then.
So we start with the six. The six is greater than and I'll color that in grey.
The one is less than I'll color that in yellow, and then what we're going to 
do is swap that one with the first item that was greater.
So every yellow item we swap with the first grey item.
"""

"""
91.Pivot intro
Pivot is a helper function which we use for quicksort
We use index instead of value
"""


"""
92.Pivot code
In this function we have two different places where we need to swap items
inside of the list, but since we're doing it twice, we create a function.
"""

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
        swap(my_list, pivot_index, swap_index)
        return swap_index

my_list = [4,6,1,7,3,2,5]
print(pivot(my_list, 0, 6))
print(my_list)


"""93. Quick sort: code"""
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort(my_list))


"""
94. Quick sort: bigO
Pivot part - O(n)
Recursive part - O(log n)
So time complexity - O(n * log n) - for best and average case, 
O(n^2) - for worst case, if you have already sorted data
For already sorted data is best to use insertion sort - O(n)
Space comlpexity - O(1)
"""
