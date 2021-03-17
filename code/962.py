from collections import deque
from typing import *
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:

        s=[]
        N=len(A)
        for i in range(N):
            if not s or A[s[-1]]>A[i]:
                s.append(i)
        res=0
        for i in range(N)[::-1]:
            while s and A[i]>=A[s[-1]]:
                res=max(res,i-s.pop())
        return res

if __name__ =='__main__':
    sol=Solution()
    # print(sol.maxWidthRamp([29,28,27,27,22,22,20,16,16,13,13,12,10,8,8,8,8,6,5,4,4,3,3,2,2,2,1,1,1,0]))
    print(sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))