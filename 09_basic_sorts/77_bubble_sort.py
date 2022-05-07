def bubble_sort(my_list): # O(n^2)
    for i in range(len(my_list)-1, 0, -1): # from 5(6-1) to 0 -1(decrement) - each next step my_list decrements to 1 item from the end
        for j in range(i): # run 5 times for 5 comparisons, then 4 times and so on
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([4,2,6,5,1,3]))
