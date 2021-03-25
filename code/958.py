import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q=collections.deque([(root)])
        
        prev_node=root
        
        while q:
            node=q.pop()
            
            
            if node and not prev_node:
                return False
            if not node:
                prev_node=node
                continue
            
            q.appendleft(node.left)
            q.appendleft(node.right)
            prev_node=node
        return True
            
            
        