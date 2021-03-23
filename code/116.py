from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
#         head=Node()
#         head.next=root
#         q=collections.deque([(0,root)])
#         prev_node=root
#         prev_level=-1
        
#         while q:
#             level,node=q.pop()
#             if not node:
#                 continue
#             q.appendleft((level+1,node.left))
#             q.appendleft((level+1,node.right))
#             if level==prev_level:
#                 prev_node.next=node
#             else:
#                 prev_node.next=None
        
        
#             prev_level=level
#             prev_node=node
#         return head.next

        # true O(1) space
        node=root
        while node and node.left:
            next_level=node.left
            while node:
                node.left.next=node.right
                node.right.next = node.next.left if node.next else None
                node=node.next
            node=next_level
        return root

        
