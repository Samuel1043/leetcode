from typing import *
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for _ in range(n)] for _ in range(n)]

        top=0
        bot=n-1
        left=0
        right=n-1
        cnt=1

        while bot>=top and right>=left:

            for i in range(left,right+1):
                ans[top][i]=cnt
                cnt+=1
            top+=1

            for i in range(top,bot+1):
                ans[i][right]=cnt
                cnt+=1
            right-=1

            if bot>=top:
                for i in range(right,left-1,-1):
                    ans[bot][i]=cnt
                    cnt+=1
                bot-=1
            if right>=left:
                for i in range(bot,top-1,-1):
                    ans[i][left]=cnt
                    cnt+=1
                left+=1
        return ans
if __name__ =='__main__':
    sol=Solution()
    print(sol.generateMatrix(3))