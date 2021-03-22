import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        q=collections.deque([(root,0)])
        ans_level=None
        # index of the current node 
        cnt=0
        
        while q:
            cnt+=1
            node,level=q.pop()
            # if only one ans_level exist(may be x or y), then 
            # return False if current level is larger than ans_level
            if ans_level!=None and level>ans_level:
                return False
            if not node:
                continue
            val=node.val
            q.appendleft((node.left,level+1))
            q.appendleft((node.right,level+1))
            # get ans_level id val equal to x or y
            if val==x or val==y:
                # get the first exist ans_level
                if ans_level==None:
                    ans_level=level
                    prev_cnt=cnt
                # compare the second exist ans_level with first exist ans_level
                else :
                    if ans_level==level:
                        # check if they have same parent
                        if cnt!=prev_cnt+1:
                            return True
                        else:
                            if cnt%2==0:
                                return True