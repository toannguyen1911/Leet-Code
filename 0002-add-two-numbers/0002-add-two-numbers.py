# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        s1, s2 = 0, 0
        i = 0
        while(temp1):
            s1 += temp1.val* (10**i)
            temp1 = temp1.next
            i+= 1
        j = 0
        
        while(temp2):
            s2 += temp2.val* (10**j)
            temp2 = temp2.next
            j+= 1
        result = list(str(s1 +s2))
        
        total = ListNode(val = result[len(result)-1])

        a = total
        
        if len(result)>1:
            for i in range(1, len(result)):
                a.next = ListNode(val = result[len(result) - i - 1])
                a = a.next
        return total
        
        