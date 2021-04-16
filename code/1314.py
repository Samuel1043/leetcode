import math
from typing import *
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M=len(mat)
        N=len(mat[0])
        # dp[i][j] sum for the rectangle shape of [0][0] to [i][j]
        dp=[[0 for _ in range(N)] for _ in range(M)]
        for row in range(M):
            total=0
            for col in range(N):
                total+=mat[row][col]
                dp[row][col]=total
                if row>0:
                    dp[row][col]+=dp[row-1][col]
        # https://leetcode.com/problems/matrix-block-sum/discuss/482730/Python-O(-m*n-)-sol.-by-integral-image-technique.-90%2B-with-Explanation
        ans=[[0 for _ in range(N)] for _ in range(M)]
        for row in range(M):
            for col in range(N):
                left_col=max(col-k,0)
                right_col=min(N-1,col+k)
                bot_row=min(M-1,row+k)
                top_row=max(0,row-k)
                ans[row][col]=dp[bot_row][right_col]
                if left_col>0:
                    ans[row][col]-=dp[bot_row][left_col-1]
                if top_row>0:
                    ans[row][col]-=dp[top_row-1][right_col]
                if top_row>0 and left_col>0:
                    ans[row][col]+=dp[top_row-1][left_col-1]
        return ans

if __name__ =='__main__':
    sol=Solution()
    print(sol.matrixBlockSum( mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))