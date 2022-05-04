"""
Two cases:
- base case - result when we stop recursion
- recursive case - when we continue call the function itself

Basic rules for recursion:
- you need to be doing the same thing over and over.
- the problem needs to be getting smaller until you finally get to a base case.
"""

"""75.Call Stack
"""
def func_three():
    print('three')

def func_two():
    func_three()
    print('two')
    
def func_one():
    func_two()
    print('one')

func_one()
