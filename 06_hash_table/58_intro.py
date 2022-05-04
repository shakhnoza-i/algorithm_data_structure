"""
Built-in hash table, which is dictionaries.

Hash storing
The way a hash table works is this we need a hash function or a hash method, and 
what we're going to do is perform a hash on the key. So we take that key, run it 
through the hash, and in addition to getting our key value pair back, we get address.
The address where we store that key value pair and that is how a dictionary is stored.

Hash characteristics:
- One way: we run dict through the hash and we get the number, but we can't do it reverse
- Deterministic: means that for a particular hash function, every time we put nails in, 
we expect to get the number two every time.
So even though Python includes a hash table, which is dictionaries, we're going to 
build our own, we'll create our own address space by creating a list and then we'll 
create methods, which store out key value pair in hash table. 
In one address, we can store multiple key value pairs
"""