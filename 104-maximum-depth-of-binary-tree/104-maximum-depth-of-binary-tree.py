# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def Tree(root, depth):
            if not root: return depth
            return max(Tree(root.left, depth +1), Tree(root.right, depth +1))
        return Tree(root, 0)
    #DFS