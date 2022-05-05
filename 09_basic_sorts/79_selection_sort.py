"""
Selection sort
- take first element (index = 0)
- compare to each element tof find minimum
- swap minimum element and first element
"""

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)): # length is 6, so index is 5
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:    
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([4,2,6,5,1,3]))
