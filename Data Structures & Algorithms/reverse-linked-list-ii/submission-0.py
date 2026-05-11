# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # First phase, go to the 
        leftofprev = dummy
        cur = head
        for _ in range(left-1):
            leftofprev, cur = cur, cur.next
        # Reverse the linked list 
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # Reversed, now deal with linking
        leftofprev.next.next = cur
        leftofprev.next = prev
        return dummy.next
