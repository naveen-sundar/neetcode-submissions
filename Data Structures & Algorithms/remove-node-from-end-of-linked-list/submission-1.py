#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        c = 1
        dummy = ListNode(0)
        dummy.next = prev
        new_prev = dummy
        new_cur = prev
        while c <= n:
            if c == n:
                new_prev.next = new_cur.next
                break
            else:
                temp = new_cur.next
                new_prev = new_cur
                new_cur = temp
                c += 1
        
        n_cur = dummy.next
        n_prev = None
        while n_cur:
            temp = n_cur.next
            n_cur.next = n_prev
            n_prev = n_cur
            n_cur = temp
        
        return n_prev
