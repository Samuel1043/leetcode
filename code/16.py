from typing import *
inf=float('inf')
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N=len(nums)
        nums.sort()
        ans=inf
        for i in range(N):
            if i>0 and nums[i]==nums[i-1]: continue
            
            j=i+1
            k=N-1
            while j<k:
                cur=target-(nums[i]+nums[j]+nums[k])
                if abs(cur)<abs(ans):
                    ans=cur
                if  cur>0:
                    j+=1
                elif cur<0:
                    k-=1
                else:
                    return target-cur
        return target-ans
            
            
if __name__ =='__main__':
    sol=Solution()
    print(sol.threeSumClosest([-1,2,1,-4],1))