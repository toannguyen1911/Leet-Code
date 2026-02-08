# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1;
    
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0;

        left_height = self.getHeight(node.left);
        if left_height == -1:
            return -1;  # The left subtree is unbalanced
        
        right_height = self.getHeight(node.right);
        if right_height == -1:
            return -1;  # The right subtree is unbalanced
        
        if abs(left_height - right_height) > 1:
            return -1;

        return max(left_height, right_height) +1;
        