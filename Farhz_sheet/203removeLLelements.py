# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prev  =  None
        curr = head
        while(curr):
            if(curr.val == val and prev):
                prev.next=curr.next
                curr  = curr.next 
                continue
            elif(curr.val ==  val  and not prev):
                head = curr.next
                curr = curr.next
                continue
            prev=curr
            curr = curr.next
        #we are directly manipulating in place so we return head ,becuase we will have direct object address
        return head
        