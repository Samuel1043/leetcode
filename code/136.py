from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur=0
        for num in nums:
            cur=num ^ cur
        return cur

if __name__ =='__main__':
    sol=Solution()
    print(sol.singleNumber([4,1,2,1,2]))
