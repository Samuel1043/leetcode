from typing import *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M=len(matrix)
        N=len(matrix[0])
        top=0
        bot=M-1
        left=0
        right=N-1
        i=0
        j=0
        ans=[]

        while left<=right and top<=bot:
            while j<=right:
                ans.append(matrix[i][j])
                j+=1
            i+=1
            j-=1
            top+=1
            while i<=bot:
                ans.append(matrix[i][j])
                i+=1
            j-=1
            i-=1
            right-=1
            if top<=bot:
                while j>=left:
                    ans.append(matrix[i][j])
                    j-=1
                i-=1
                j+=1
                bot-=1
            if left<=right:
                while i>=top:
                    ans.append(matrix[i][j])
                    i-=1
                j+=1
                i+=1
                left+=1

        return ans
if __name__ =='__main__':
    sol=Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))