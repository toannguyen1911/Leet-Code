# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(1)
        """
        nums_set = set(nums);
        pre_head = ListNode(0, head);
        node = pre_head;
        
        while (node.next):
            if node.next.val in nums_set:
                node.next = node.next.next;
            else:
                node = node.next;

        return pre_head.next;