"""
bigO - to compare two solutions
Time comlpexity - it is measured in the number of operations performed
Space comlpexity - measured by size of memory space is taken for operations

5. BigO: worst case
O - omicron (algorithm and data structure efficiency in worst case) like lim->∞

7. BigO: drop constants
For O(2n) - we drop constants so O(2n)->O(n) so the constant value doesn't matter

8. BigO: O(n^2)
Example for O(n^2) - when we have 1 for loop inside another. O(n^3)->O(n^2)

9. BigO: drop non-dominants
O(n^2) + O(n) -> O(n^2 + n) -> O(n^2)

10. BigO: O(1) - constant time - most efficient

11. BigO: O(log(n))
"""


# 12. BigO: different terms for inputs

def print_items(a, b): # O(a+b)
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

def print_items(a, b): # O(a*b)
    for i in range(a):
        for j in range(b):
            print(i, j)


# 13. BigO: Lists - O(n)
my_list = [18, 25, 12] 
#  it doesn't matter if you're removing or if you're adding to a list - O(n)

"""
14. BigO: Wrap Up
O(n^2) - loop within a loop
O(n) - proportinal
O(log(n)) - divide and conquer
O(1) - constant
"""