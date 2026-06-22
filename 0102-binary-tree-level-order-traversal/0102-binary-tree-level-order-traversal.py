class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        result = []
    
        queue = [root]
        
        while len(queue) > 0:
            level_size = len(queue)
            current_level = []
            
            for i in range(level_size):
              
                node = queue.pop(0) 
               
                current_level.append(node.val)
               
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            result.append(current_level)
            
        return result