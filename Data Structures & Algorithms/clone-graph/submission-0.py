# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        # Each node's integer value
        self.val = val
        # List of neighboring nodes
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # If graph is empty, return None
        if not node:
            return None

        # Dictionary to map original nodes to their clones
        visited = {}

        # Recursive DFS function to clone nodes
        def dfs(current):
            # If node already cloned, return it
            if current in visited:
                return visited[current]

            # Create clone of current node
            clone = Node(current.val)
            # Store clone in visited map
            visited[current] = clone

            # Recursively clone all neighbors
            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start DFS from given node
        return dfs(node)