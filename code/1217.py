from typing import *

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        dividedby2=0
        for num in position:
            if num%2==0:
                dividedby2+=1
        
        return min(dividedby2,len(position)-dividedby2)