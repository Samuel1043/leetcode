from typing import *

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res=0
        largest=0
        for rec in rectangles:
            cur=min(rec[0],rec[1])
            if cur>largest:
                largest=cur
                res=1
            elif cur==largest:
                res+=1
            else:
                pass
        return res