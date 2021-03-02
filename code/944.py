from typing import *
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        total=0
        for i in range(len(strs[0])):
            prev='a'
            for j in range(len(strs)):
                cur=strs[j][i]
                if prev>cur:
                    total+=1
                    break
                prev=cur
        return total