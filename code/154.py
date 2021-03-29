from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        N=len(nums)
        start=0
        end=N-1
        
        while start<end:
            
            mid=(start+end)//2
            
            while nums[mid]==nums[end] and mid<end:
                end-=1
            
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        print(start)
        return nums[start]
if __name__ =='__main__':
    sol=Solution()
    print(sol.findMin([2,2,2,0,1]))
    print(sol.findMin([2,2,2,0,1,2]))
    print(sol.findMin([2,2,2,2,2,1,1,2]))
    print(sol.findMin([1,2,2,1,1,1,1,1,1,1]))

