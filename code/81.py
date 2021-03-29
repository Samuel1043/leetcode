class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N=len(nums)
        start=0
        end=N-1
        
        while start<=end:
            mid=(start+end)//2
            
            if nums[mid]==target:
                return True
            
            while nums[start]==nums[mid] and start<mid:
                start=start+1
            
            if nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
