from typing import *
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        
        total=sum(nums)
        target=total//4
        N=len(nums)
        if total%4!=0 or N<4: 
            return False

        # sort by descending order to speed up 
        nums.sort(reverse=True)
        # square
        edge=[0]*4

        def dfs(index):
            if index==N:
                return True
            for i in range(4):
                # sort will make this faster
                if edge[i]+nums[index]<=target:
                    edge[i]+=nums[index]
                    if dfs(index+1):
                        return True
                    edge[i]-=nums[index]
                    # speed up: 
                    # if current nums[index] can't be in edge[i] than 
                    # puuting it in edge[i+1] won't satisfy either
                    if edge[i]==0: break
            return False
        return dfs(0)


    def makesquare_dp(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Number of matchsticks
        L = len(nums)
        # perimeter of square
        perimeter = sum(nums)
        # If there are no matchsticks, then we can't form any square.
        if L<4 or perimeter%4:
            return False
        # side of square
        possible_side=perimeter // 4

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):
            # This will calculate the total sum of matchsticks 
            # used till now using the bits of the mask.
            # ex: 11111 for not using any matchsticks
            #  10010 for using idx=[1,2,4] matchsticks
            total=0
            for i in range(L):
                if not (mask & 1<<i):
                    total+=nums[i]

            if total>0 and total%possible_side==0: 
                sides_done+=1

            if sides_done==3: return True

            if (mask,sides_done) in memo:
                return memo[(mask,sides_done)]

            ans=False
            # calculate the remain space for current edge
            c=int(total/possible_side)
            rem=possible_side*(c+1)-total


            for i in range(L):
                # check if available matchsticks can fit in remain space
                if nums[i]<=rem and mask & 1<<i:
                    # return True if condition satisfy
                    if recurse(mask ^ 1<<i,sides_done):
                        return True
            
            memo[(mask,sides_done)]=ans
            return ans

        # initialize the bitmap with all 1 in bit
        #  ex: L=3 initialize:bit(111)=7
        return recurse((1 << L) - 1, 0)
if __name__ =='__main__':
    sol=Solution()
    print(sol.makesquare([5,4,1,3,2,4,1]))
    print(sol.makesquare_dp([1,2,3,3,3,4]))



























