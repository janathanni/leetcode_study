# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def pathSum(root, sum):
            #1 . 일단은 루트에서 리프까지 닿아야 함. 
            #2.  리프인 거랑, 코드상에서 left, right로 None인 거랑은 다름. 
            if root is None:
                return False

            if root.left or root.right :
                return pathSum(root.left, sum + root.val) or pathSum(root.right, sum + root.val)
            
            if root.left is None and root.right is None and root: #leaf일 경우 
                if (sum + root.val) == targetSum:
                    return True 
                
                else:
                    return False
        
        return pathSum(root, 0)        