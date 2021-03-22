import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q=collections.deque([(root,0)])
        prev_level=0
    
        res=[]
        tmp=[]
        while q:
            node,level=q.pop()
            if not node:
                continue
            val=node.val
            
            q.appendleft((node.left,level+1))
            q.appendleft((node.right,level+1))
            
            if prev_level!=level:
                if level%2==1:
                    res.append(tmp)
                else:
                    res.append(tmp[::-1])
                tmp=[val]
            else:
                tmp.append(val)
            prev_level=level
            
        if level%2==1:
            res.append(tmp)
        else:
            res.append(tmp[::-1])

        return res