from typing import *
import sys
from unionfind import Unionfind

def solve(board: List[List[str]]) -> None:
    directions=[[0,1],[0,-1],[1,0],[-1,0]]
    n_row=len(board)
    n_col=len(board[0])
    # border will union to dummy
    dummy=n_row*n_col
    # weighted quick union with path compression
    un=Unionfind(dummy+1)

    for i in range(n_row):
        for j in range(n_col):
            if board[i][j]=='O':
                pos=i*n_col+j
                if (i==0 or i==n_row-1 or j==0 or j==n_col-1):
                    un.union(pos,dummy)
                else:
                    for way in directions:
                        newi,newj=i+way[0],j+way[1]
                        if board[newi][newj]=='O':
                            newpos=newi*n_col+newj
                            un.union(pos,newpos)
    for i in range(n_row):
        for j in range(n_col):
            pos=i*n_col+j
            if board[i][j]=='O' and not un.connected(pos,dummy):
                board[i][j]='X'
    return board


    # quick union runtime exception
    # connected_sets=[]
    # directions=[[0,1],[0,-1],[1,0],[-1,0]]
    # n_row=len(board)
    # n_col=len(board[0])
    # for i in range(n_row):
    #     for j in range(n_col):
    #         if board[i][j]=='O':
    #             pos=i*n_col+j
    #             if connected_sets:
    #                 merge_idx=[]
    #                 for idx in range(len(connected_sets)):
    #                     if pos in connected_sets[idx]:
    #                         merge_idx.append(idx)
    #                 if merge_idx:
    #                     new_set=set()
    #                     for idx in sorted(merge_idx,reverse=True):
    #                         for ele in connected_sets[idx]:
    #                             new_set.add(ele)
    #                         del connected_sets[idx]
    #                     connected_sets.append(new_set)
    #                 else:
    #                     connected_sets.append(set([pos]))
    #             else:
    #                 connected_sets.append(set([pos]))
                
    #             for direction in directions:
    #                 newRow,newCol=i+direction[0],j+direction[1]
    #                 if (newRow>=0 and newRow<=n_row-1 and newCol>=0 and newCol<=n_col-1 and board[newRow][newCol] == 'O'):
    #                     newPos=newRow*n_col+newCol
    #                     for idx in range(len(connected_sets)):
    #                         if pos in connected_sets[idx]:
    #                             connected_sets[idx].add(newPos)

    # for i in range(n_row):
    #     for j in range(n_col):
    #         board[i][j] ='X'
    # for i in range(n_row):
    #     for j in range(n_col):
    #         if i!=0 and j!=0 and j!=n_col-1 and i!=n_row-1:
    #             continue
    #         num=i*n_col+j 
    #         for num_set in connected_sets:
    #             if num in num_set:
    #                 for connect_num in num_set:
    #                     row=connect_num//n_col
    #                     col=connect_num%n_col
    #                     board[row][col]='O'
    # return board







solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solve([["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]])