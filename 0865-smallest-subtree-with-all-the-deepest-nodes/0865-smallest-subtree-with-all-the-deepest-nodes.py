# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return None, 0;

        left_node, left_depth = self.dfs(node.left);
        right_node, right_depth = self.dfs(node.right);

        if left_depth == right_depth:
            return node, left_depth + 1;
            
        if left_depth > right_depth:
            return left_node, left_depth + 1;

        return right_node, right_depth + 1;

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node, _ = self.dfs(root);

        return node;