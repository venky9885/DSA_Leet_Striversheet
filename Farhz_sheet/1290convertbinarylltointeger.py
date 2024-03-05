# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #too easy
        st = ''
        while(head):
            st+=str(head.val)
            head = head.next
        print(st)
        return int(st,2)
        