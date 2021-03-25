import collections
from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        M=len(grid)
        N=len(grid[0])

#         DFS
#         def dfs(pos):
#             if grid[pos[0]][pos[1]]=='0':
#                 return 
#             grid[pos[0]][pos[1]]='0'
#             for direction in directions:
#                 cur_row=pos[0]+direction[0]
#                 cur_col=pos[1]+direction[1]
#                 if cur_row>M-1 or cur_col>N-1 or cur_row<0 or cur_col<0:
#                     continue
#                 dfs((cur_row,cur_col))
                
#         ans=0
#         for row in range(M):
#             for col in range(N):
#                 if grid[row][col]=='1':
#                     dfs((row,col))
#                     ans+=1
#         return ans

        # BFS
        ans=0
        for row in range(M):
            for col in range(N):
                if grid[row][col]=='1':
                    q=collections.deque([(row,col)])
                    while q:
                        cur_row,cur_col=q.pop()
                        if grid[cur_row][cur_col]=='0':
                            continue
                        
                        grid[cur_row][cur_col]='0'
                        for direction in directions:
                            next_row,next_col=cur_row+direction[0],cur_col+direction[1]
                            if next_row>M-1 or next_col>N-1 or next_row<0 or next_col<0 or grid[next_row][next_col]=='0':
                                continue
                            q.appendleft((next_row,next_col))
                        
                    
                    ans+=1
        return ans