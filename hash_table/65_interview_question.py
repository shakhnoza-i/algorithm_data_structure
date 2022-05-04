"""
In 2 lists which item is most common: 
list1 = [1, 3, 5], list2 = [2, 4, 5]

Naive method - obvious approach would be to create nested for loops.
So we'll have one for loop to go through the first list, then a 
second one to compare all the items in the second list to that number.
This method is not efficient - O(n^2)

Better approach:
{
    1: True,
    3: True,
    5: True
}
Now we will loop through the second list to compare the first key to the dictionary 
to see is the first key in the dictionary. 
So we had to go through each list once - O(2n) ->O(n)
"""

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False
