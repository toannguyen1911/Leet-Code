# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = ListNode(val = head.val)

        temp = head.next
        count = 1
        while(temp != None):
            count +=1
            new_node = ListNode(temp.val, node)
            node = new_node
            temp = temp.next
        
        if count <= 2:
            return
        if count ==3:
            head.next = ListNode(new_node.val)
            head.next.next = ListNode(new_node.next.val)
            return
        
        temp = ListNode(head.next.val, head.next.next)
        if count % 2 != 0:
            i = count//2 +1
        else: i = count//2
        
        head.next = ListNode(new_node.val)
        head = head.next
        new_node = new_node.next
        while (i -1):
            print(i)
            head.next = ListNode(temp.val)
            head = head.next
            #print(temp)
            #print("new", new_node)
            head.next = ListNode(new_node.val)
            head = head.next
            i -=1      
            if count %2 != 0 and i == 2 :
                #print(i)
                head.next = temp.next
                head.next.next = None
                break
                                
            new_node = new_node.next
            temp = temp.next
           
        