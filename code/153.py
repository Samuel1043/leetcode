from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:

        N=len(nums)
        start=0
        end=N-1

        while start<end:
            mid=(start+end)//2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        print(nums[start],nums[end])

if __name__ =='__main__':
    sol=Solution()
    sol.findMin([4,5,0,1,2,3])
