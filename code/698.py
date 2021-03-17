from typing import *

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or sum(nums) % k != 0 or max(nums) > sum(nums) //k:
            return False

        target=sum(nums)//k
        nums.sort(reverse=False)
#         square
        edge=[0]*k

        def dfs(index):
            if index==len(nums):
                return len(set(edge+[target])) == 1
            for i in range(k):
                if edge[i]+nums[index]<=target:
                    edge[i]+=nums[index]
                    if dfs(index+1):
                        return True
                    edge[i]-=nums[index]
                    if edge[i] == 0: break
            return False
        return dfs(0) 

    def canPartitionKSubsets_dp(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        arr_sum=sum(nums)
        
        if N<k or arr_sum%k!=0: return False

        side=arr_sum//k
        memo={}

        def recurse_dp(mask,cur_k):
            total=0
            for i in range(k):
                if not mask&1<<i:
                    total+=nums[i]


            if total%side==0 and total>0:
                cur_k+=1
            
            if cur_k==k-1:
                return True
            if (mask,cur_k) in memo:
                return False

            rem=side*(total//side+1)-total

            for i in range(k):
                if rem>=nums[i] and mask&1<<i:
                    if recurse_dp(mask^1<<i,cur_k):
                        return True
            memo[(mask,cur_k)]=False
            return False







if __name__ =='__main__':
    sol=Solution()
    print(sol.canPartitionKSubsets([1,2,3],2))