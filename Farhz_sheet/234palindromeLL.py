# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#very easy understand better
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #retrive mid point with fast and slow it stops excatly at middile
        sp,fp = head,head
        while(fp and fp.next):
            fp = fp.next.next
            sp = sp.next
        # print(sp,fp)
        # reverese the secnod half because pointer is in sp
        #this code is also used for reversing ll
        prev,cur = None,sp
        while(cur):
            newNode = cur.next
            cur.next = prev
            prev =  cur
            cur = newNode
        
        firstHalf,reversedHalf = head,prev
        while(firstHalf  and reversedHalf):
            if(firstHalf.val != reversedHalf.val):
                return False
            firstHalf=firstHalf.next
            reversedHalf= reversedHalf.next
        return True

        
#simple solution dont us ethis
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = ''
        while(head):
            st+=str(head.val)
            head = head.next
        return st == st[::-1]