"""
Space complexity between Adjacency Matrix(AM) and Adjacency List(AL)
So a huge difference between AL and AM is that in a matrix, each vertex
has to store all of the vertices it is not connected to.
AM - O(|V|^2) - number of vertices squared
AL - O(|V|+|E|) - number of vertices plus the number of edges

Adding new vertex:
AM - O(|V|^2)
AL - O(1)

Adding edge:
AM - O(1)
AL - O(1)

Removing edge:
AM - O(1)
AL - O(E) - need to go through all the edges of list, find F and remove it.

Remove vertex:
AM - O(|V|^2)
AL - O(V|+|E|) - need to remove all of the other edges so the vertex could have

AM - we're not only storing the ones(weights), we're also storing the zeros, so
it's incredibly inefficient from a storage perspective.
So we use AL in this course
"""