from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol=0
        start=0
        end=len(height)-1
        while end>start:
            max_vol=max(max_vol,(end-start)*min(height[end],height[start]))
            
            if height[end]>height[start]:
                start+=1
            else:
                end-=1
                
        return max_vol

if __name__ =='__main__':
    sol=Solution()
    print(sol.maxArea([4,3,2,1,4]))
    print(sol.maxArea([1,2,1]))
    print(sol.maxArea([1,2,0]))
    print(sol.maxArea([0,2,0]))
    print(sol.maxArea([1,8,9,100,4,9,8,7]))
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

