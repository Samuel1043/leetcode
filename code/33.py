class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N=len(nums)
        start=0
        end=N-1

        # # find the change rotating point of array
        # while start<end:
        #     mid=(start+end)//2
        #     if nums[mid]>nums[end]:
        #         start=mid+1
        #     else:
        #         end=mid

        # def bs(arr,target):
        #     n=len(arr)
        #     start=0
        #     end=n-1
        #     while start<=end:
        #         mid=(start+end)//2
        #         if arr[mid]>target:
        #             end=mid-1
        #         elif arr[mid]<target:
        #             start=mid+1
        #         else:
        #             return mid
        #     return -1
        
        # # compare front arr if target larger
        # if target>nums[-1]:
        #     res=bs(nums[:start],target)
        #     if res==-1:
        #         return -1
        #     else:
        #         return res
        # # compare back arr if target smaller
        # elif target<nums[-1]:
        #     res=bs(nums[start:],target)
        #     if res==-1:
        #         return -1
        #     else:
        #         return res+start
        # # if smae return idx
        # else:
        #     return N-1    
        
        while start<=end:
            mid=(start+end)//2
            if target==nums[mid]:
                return mid
            if nums[mid]==nums[start]


            # first half order
            if nums[mid]>=nums[start]:
                if nums[mid]>target>=nums[start]:
                    end=mid-1
                else:
                    start=mid+1
            # second half order
            else:
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
                
