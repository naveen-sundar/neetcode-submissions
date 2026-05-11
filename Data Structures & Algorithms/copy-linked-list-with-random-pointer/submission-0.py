"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToHead = {None: None}
        cur = head
        
        while cur:
            copy = Node(cur.val)
            oldToHead[cur] = copy
            cur = cur.next # Each node points to a dummy node
        
        cur = head
        
        while cur:
            
            copy = oldToHead[cur]
            copy.next = oldToHead[cur.next]
            copy.random = oldToHead[cur.random]

            cur = cur.next
        return oldToHead[head]