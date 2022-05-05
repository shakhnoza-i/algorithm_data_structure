"""
In DFS postorder we start add value of node if it doesn't have childs.
And we always start from left bottom
"""

def dfs_postorder(self):
    results = []
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.value)
    traverse(self.root)
    return results
