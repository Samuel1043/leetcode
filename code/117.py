# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node=root
        # if exist next level
        while node:
            # store prev node to point
            prev_node=None
            # iterate over one level
            while node:
                for i in [node.left, node.right]:
                    # continue if node point to None
                    if not i:
                        continue
                    # get the next level's first nodes
                    # and store the node as prev_node
                    if not prev_node:
                        next=i
                        prev_node=i
                    # assign pre_node next is node
                    else:
                        i.next=prev_node
                        prev_node=i
                node=node.next
            # assign 
            node=next