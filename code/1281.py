class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        add=0
        for num in str(n):
            num=int(num)
            mul*=num
            add+=num
        return mul-add