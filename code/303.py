class NumArray:

    def __init__(self, nums: List[int]):
        self.dp=[0]*len(nums)
        total=0
        for idx,num in enumerate(nums):
            total+=num
            self.dp[idx]=total

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.dp[right]
        else:
            return self.dp[right]-self.dp[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)