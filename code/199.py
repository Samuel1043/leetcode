# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        q=collections.deque([(0,root)])
        prev_node=root
        prev_level=0
        res=[]
        while q:
            level,node=q.pop()
            if not node:
                continue
            q.appendleft((level+1,node.left))
            q.appendleft((level+1,node.right))
            if level!=prev_level:
                res.append(prev_node.val)        
        
            prev_level=level
            prev_node=node
        res.append(prev_node.val)
        return res