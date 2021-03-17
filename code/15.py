from typing import *
import collections
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        
        ans=[]
        nums.sort()
        for i in range(N):
            # don't calculate same value again
            if i>0 and nums[i]==nums[i-1]: continue
            target=nums[i]
            value_map=collections.defaultdict(int)
            for j in range(i+1,N):
                if nums[j] in value_map:
                    # check if current nums is used
                    if value_map[nums[j]]==True:
                        value_map[nums[j]]=False
                        ans.append([nums[i],nums[j],-(nums[j]+target)])   
                    continue
                value_map[-(target+nums[j])]=True
        
        return ans
            
if __name__ =='__main__':
    sol=Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))