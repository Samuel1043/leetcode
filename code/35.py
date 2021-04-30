class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def BS(arr,tar):

            start=0
            end=len(arr)-1
            while start<=end:
                mid=(start+end)//2
                if arr[mid]>tar:
                    end=mid-1
                elif arr[mid]<tar:
                    start=mid+1
                else:
                    return mid
            return start

        return BS(nums,target)
