# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = str(root.val)
        if not root:
            string += ""
        else:
            if root.left:
                string += "(" + self.tree2str(root.left) + ")"
            else: string += "()" if root.right else ""
            if root.right:
                string += "(" + self.tree2str(root.right) + ")"
            else: string += ""
        return string
        