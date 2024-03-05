# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #!its tooooo easy
        ct = 0
        temp  =  head
        while(temp):
            temp =  temp.next
            ct+=1
        ct = ct//2
        while(ct ):
            print(head.val)
            head = head.next
            ct-=1
        return head
        
        