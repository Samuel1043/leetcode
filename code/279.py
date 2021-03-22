import math
from collections import deque
inf=float('inf')
class Solution:
    def numSquares(self, n: int) -> int:
    #     #   dp
    #     square_dp=[0]
    #     while len(square_dp)<=n:
    #         m=len(square_dp)
    #         cur_square_cnt=inf
    #         for i in range(1,int(math.sqrt(m))+1):
    #             cur_square_cnt=min(cur_square_cnt,square_dp[m-i**2]+1)
    #         square_dp.append(cur_square_cnt)
    #     return square_dp[-1]
    
    
    # BFS
        can_square=[]
        
        i=1
        while i**2<n:
            can_square.append(i**2)
            i+=1
        can_square=can_square[::-1]
        q=deque([(n,1)])
        
        while q:
            print(q)
            val,level=q.pop()

            for num in can_square:
                if val-num==0:
                    return level
                q.appendleft((val-num,level+1))
        
                
                

if __name__ =='__main__':
    sol=Solution()
    print(sol.numSquares(10))




