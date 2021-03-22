import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        q=collections.deque([(root,0)])
        prev_level=0
        tmp=[]
        res=[]
        
        while q:
            node,level=q.pop()
            if not node:
                continue
            q.appendleft((node.left,level+1))
            q.appendleft((node.right,level+1))
            
            if prev_level!=level:
                res.append(sum(tmp)/len(tmp))
                tmp=[node.val]
                
            else:
                tmp.append(node.val)
                
            prev_level=level
            
        res.append(sum(tmp)/len(tmp))
        return res
            
            