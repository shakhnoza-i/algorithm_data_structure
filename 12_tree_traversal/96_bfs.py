"""
BFS: Breadth First Search was the one where we would start at the top 
and then do the second row straight across and so on

Stages: 
queue list - we save entire node(with value and left and right)
result list - only values

We implement BFS using usual lists, but the best choice is LinkedList
"""

def bfs(self):
    current_node = self.root
    results = []
    queue = []
    queue.append(current_node)
    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return results
