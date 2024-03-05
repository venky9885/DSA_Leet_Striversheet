# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#for better explantion https://youtu.be/VtC4GUR31wQ
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        cur = head
        #we use 3 vars temp is newLL ,cur pointer to manipulate links,nextNode to point new node LL
        while(cur):
            #first set nextNode link to cur . next
            nextNode = cur.next
            #point cur . neext to temp
            cur.next = temp
            #point head of new LL to temp which is present in cur
            temp = cur
            #after using cur set it to next node
            cur = nextNode
        return temp

        
            