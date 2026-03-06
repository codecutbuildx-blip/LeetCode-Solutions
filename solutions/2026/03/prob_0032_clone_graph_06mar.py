from typing import List, Optional

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Approach: 
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Create a dictionary to store the nodes we've seen so far
        visited = {}
        
        # Define a helper function to perform DFS
        def dfs(node):
            # If the node is None, return None
            if node is None:
                return None
            
            # If we've seen this node before, return the cloned node
            if node in visited:
                return visited[node]
            
            # Create a new node
            new_node = Node(node.val)
            
            # Mark the new node as visited
            visited[node] = new_node
            
            # Recursively clone the neighbors
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            # Return the cloned node
            return new_node
        
        # Start the DFS from the root node
        return dfs(node)