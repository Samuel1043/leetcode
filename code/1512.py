from typing import *
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # cnt=Counter()
        # res=0
        # for num in nums:
        #     if num in cnt:
        #         res+=cnt[num]
        #         cnt.update([num])            
        #     else:    
        #         cnt.update([num])
        # return res

        cnt=Counter(nums)
        
        return sum((k)*(k-1)//2 for k in cnt.values())

if __name__ =='__main__':
    sol=Solution()
    print(sol.numIdenticalPairs([1,1,1,1]))
    print(sol.numIdenticalPairs([1]))
