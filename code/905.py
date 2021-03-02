from typing import *
def sortArrayByParity(self, A: List[int]) -> List[int]:
    N=len(A)
    i=0
    j=N-1
    while i<j:
        cur=A[i]
        if cur%2==0:
            i+=1
        else:
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
            j-=1
    return A