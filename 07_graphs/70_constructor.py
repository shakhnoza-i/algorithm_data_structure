"""70.Graph: Add Vertex"""
class Graph:

    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    """71.Graph: Add Edge"""
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    """72.Graph: Remove Edge"""
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    """73.Graph: Remove Vertex"""
    # in bidirectional connections and the efficiency is contained in this list -
    # if D has an edge with another vertex, that vertex also has an edge with D.
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()

my_graph.add_vertex('A') # A:[]
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.print_graph()

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.remove_edge('B', 'C')
my_graph.remove_vertex('B')
