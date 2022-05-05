"""
In DFS InOrder all values written to list in numerical order
"""

def dfs_inorder(self):
    results = []
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)
    traverse(self.root)
    return results
