class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1=len(text1)
        N2=len(text2)
        # top down
        # if N2>N1:
            # return longestCommonSubsequence(text2,text1)
#         memo={}
#         def findlongest(idx1,idx2):
#             if (idx1,idx2) in memo:
#                 return memo[(idx1,idx2)]
#             if idx1==N1 or idx2==N2:
#                 val=0
#             elif text1[idx1]==text2[idx2]:
#                 val=1+findlongest(idx1+1,idx2+1)
#             else:
#                 val=max(findlongest(idx1+1,idx2),findlongest(idx1,idx2+1))
#             memo[(idx1,idx2)]=val
#             return val
#         return findlongest(0,0)

        # bottom up
        # store a dp for longest subsequence given different index postion
        memo=[[0 for _ in range(N2+1)] for _ in range(N1+1)]
        # start from 1
        for i in range(1,N1+1):
            for j in range(1,N2+1):
                # compare from the first postion
                if text1[i-1]==text2[j-1]:
                    val=1+memo[i-1][j-1]
                else:
                    val=max(memo[i-1][j],memo[i][j-1])
                memo[i][j]=val
        return memo[-1][-1]