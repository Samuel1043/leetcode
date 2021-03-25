from typing import *
from collections import deque
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        M=len(grid)
        N=len(grid[0])
        new_grid=[[0 for _ in range(N*3)] for _ in range(M*3)]
        for row in range(M):
            for col in range(N):
                char=grid[row][col]
                cur_row=row*3
                if char==' ':
                    continue
                elif char=='/':
                    cur_col=col*3+2
                    for i in range(3):
                        new_grid[cur_row+i][cur_col-i]=1
                elif char=='\\':
                    cur_col=col*3
                    for i in range(3):
                        new_grid[cur_row+i][cur_col+i]=1

        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        M=len(new_grid)
        N=len(new_grid[0])
        ans=0
        for row in range(M):
            for col in range(N):
                if new_grid[row][col]==0:
                    q=deque([(row,col)])
                    while q:
                        cur_row,cur_col=q.pop()
                        if new_grid[cur_row][cur_col]==1:
                            continue
                        new_grid[cur_row][cur_col]=1
                        for direction in directions:
                            next_row=cur_row+direction[0]
                            next_col=cur_col+direction[1]
                            if next_row<0 or next_col<0 or next_row>M-1 or \
                                next_col>N-1 or new_grid[next_row][next_col]==1:
                                continue
                            q.appendleft((next_row,next_col))
                    ans+=1
        return ans
if __name__ =='__main__':
    sol=Solution()
    print(sol.regionsBySlashes(["//","/ "]))

        