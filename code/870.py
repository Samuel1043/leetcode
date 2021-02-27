from typing import *
import collections
import heapq
def advantageCount(A: List[int], B: List[int]) -> List[int]:
    A.sort()
    B_idx = sorted(range(len(B)), key=lambda k: B[k])
    B.sort()

    i = 0
    back_i = -1
    j = 0
    ans = [0 for _ in range(len(A))]
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            ans[i+back_i+1] = A[i]
            i += 1
            j += 1
        else:
            ans[back_i] = A[i]
            i += 1
            back_i -= 1

    res = [0 for _ in range(len(A))]
    for idx, i in enumerate(B_idx):
        res[i] = ans[idx]
    return res

#  top solution is faster 
#   use PQ to store original idx
    # for idx,num in enumerate(B):
    #     B[idx]=[-num,idx]
    # heapq.heapify(B)
    # top=len(A)-1
    # bot=0
    # A.sort()

    # res=[0 for _ in range(top+1)]
    # print(B)
    # while B:
    #     cur,idx=heapq.heappop(B)
    #     if A[top]>-cur:
    #         res[idx]=A[top]
    #         top-=1
    #     else:
    #         res[idx]=A[bot]
    #         bot+=1

    # return res
print(advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]))
