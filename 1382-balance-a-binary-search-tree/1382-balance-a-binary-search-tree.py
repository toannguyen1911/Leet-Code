# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val;
#         self.left = left;
#         self.right = right;

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.nodes = [];
        self.inorder_traversal(root);

        return self.build_balanced_tree(0, len(self.nodes) - 1);

    def inorder_traversal(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return;

        self.inorder_traversal(node.left);
        self.nodes.append(node);
        self.inorder_traversal(node.right);

    def build_balanced_tree(self, left_index: int, right_index: int) -> Optional[TreeNode]:
        if left_index > right_index:
            return None;

        mid_index = (left_index + right_index) // 2;
        root_node = self.nodes[mid_index];
        root_node.left = self.build_balanced_tree(left_index, mid_index - 1);
        root_node.right = self.build_balanced_tree(mid_index + 1, right_index);
        
        return root_node;
