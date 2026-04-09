from typing import List, Optional
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            
            if len(result) <= level:
                result.append([])
            
            result[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return result