class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.goDepth(root, 0) 
    
    def goDepth(self, root : Optional[TreeNode], depth : int) -> int:
        if not root:
            return depth  
        
        return max(self.goDepth(root.right, depth+1), self.goDepth(root.left,  depth+1))