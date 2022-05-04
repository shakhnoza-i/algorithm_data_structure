"""
Collision happens when you put a key value pair at an address where there was already 
a key value pair. And to store second one without overwriting the first, and the way 
we're going to do that is both of these key value pairs exist within another list 
at that address. So this technique is called Separate Chaining. 
    So in another popular way of dealing with collisions, take second key value pair 
and go down until you find an empty address and you put the key value pair there. This
technique is called Linear Probing(this is form of open addressing).

We'll use Separate Chaining in this course.
Also in Separate Chaining we can use LinkedList to store within one address, but we 
use usual lists.

In priduction you're going to be dealing with a much larger address space, so 
collisions are going to be fairly rare.
"""