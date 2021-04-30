class Solution:
    def getMoneyAmount(self, n: int) -> int:

        dp=[[0 for i in range(n+1)] for i in range(n+1)]

        for num_len in range(2,n+1):
            for i in range(1,n+2-num_len):
                min_res=float('inf')
                for pivot in range(i,i+num_len-1):
                    min_res=min(min_res,pivot+max(dp[i][pivot-1],dp[pivot+1][i+num_len-1]))
                dp[i][i+num_len-1]=min_res
        print(dp)



if __name__ =='__main__':
    sol=Solution()
    sol.getMoneyAmount(3)