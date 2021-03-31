class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[1]*len(nums)

        # current idx
        for i in range(N):
            # prev idx
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)

        # def BS(arr,target):
        #     start=0
        #     end=len(arr)-1

        #     while start<=end:
        #         mid=(start+end)//2
        #         if target<arr[mid]:
        #             end=mid-1
        #         elif target>arr[mid]:
        #             start=mid+1
        #         else:
        #             return mid
        #     return start

        # sub=[]
        # for i in range(N):
        #     pos,sub_len=0,len(sub)
        #     pos=BS(sub,nums[i])
        #     print(pos,sub,nums[i])
        #     if pos==sub_len or sub_len==0:
        #         sub.append(nums[i])
        #     else:
        #         sub[pos]=nums[i]

        # return len(sub)
