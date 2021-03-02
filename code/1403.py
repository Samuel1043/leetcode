from typing import *
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total=sum(nums)
        
        res=[]
        cur=0
        for num in nums:
            cur+=num
            total-=num
            res.append(num)
            if cur>total:
                break
        return res        

if __name__ =='__main__':
    sol=Solution()
    print(sol.minSubsequence([4,4,4,4,4,7,6,7]))