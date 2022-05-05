"""
DFS - depth first search: preorder
With preorder the order that we're going to add the numbers to the list
is start in-depth in left until the end and take next node and so on in left
"""

def dfs_preorder(self):
    results = []
    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
    traverse(self.root)
    return results
