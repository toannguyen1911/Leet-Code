# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def cur(root):
            if root == None: return (0, 0)
            sumL, valL = cur(root.left)
            sumR, valR = cur(root.right)
            Cur = abs(sumL - sumR)
            return sumL + sumR + root.val, valL + valR + Cur
        return cur(root)[1]