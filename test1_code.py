import sys,os

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseNthList(self, head, k):
        if not head:
	        return None
	    
        p = head
        rtn_head = None
        phead = None
        while p:
            i = 1
            q = p.next
            while i < k and q:
                i += 1
                q = q.next
            
            if i == k:
                pstart = p
                while p.next != q:
                    ptmp = p.next
                    p.next = ptmp.next
                    ptmp.next = pstart
                    pstart = ptmp

                if not rtn_head :
                    rtn_head = pstart
                
                if not phead:
                    phead = p
                else:
                    phead.next = pstart
                    phead = p
            p = p.next
        return rtn_head

'''
if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    f = ListNode(6)
    h = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = f
    f.next = h

    sol = Solution()
    head = sol.reverseNthList(a,3)
    while head:
        print head.val
        head = head.next
'''
