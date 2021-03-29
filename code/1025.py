import math
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n<2:
            return False
        # 0 if bob win 
        dp=[0]*(n+1)
        # n equal 2 alice win
        dp[2]=1
        # iterate from 3 to n
        for i in range(3,n+1):
            # number to substaract each round
            for j in range(1,int(math.sqrt(i))+1):
                if i%j==0 and dp[i-j]==0:
                    dp[i]=1
        return dp[-1]
if __name__ =='__main__':
    sol=Solution()
    print(sol.divisorGame(10))