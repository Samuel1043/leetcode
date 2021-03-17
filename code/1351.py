from typing import *
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # def BS(left,right,val,arr):
        #     while left<right:
        #         cur=(left+right)//2
        #         # print(left,right)
        #         if arr[cur]<val:
        #             right=cur
        #         else:
        #             left=cur+1
        #     return left
        
        # N=len(grid[0])
        # res=0
        # for nums in grid:
        #     res+=(N-BS(0,N,0,nums))
        # return res

        i=len(grid)-1
        j=0
        res=0
        while i>=0 and j<=len(grid[0])-1:
            if grid[i][j]<0:
                res+=(len(grid[0])-j)
                i-=1
            else:
                j+=1
        return res
if __name__ =='__main__':
    sol=Solution()
    print(sol.countNegatives([[4,3,2,1],[4,0,0,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
