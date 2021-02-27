from typing import *

def largestSumAfterKNegations(A: List[int], K: int) -> int:
    total=0
    A=sorted(A)
    pos_idx=None
#   get first positive value idx
    for idx in range(len(A)):
        if A[idx]>=0:
            pos_idx=idx
            break
#   if K larger than first pos value idx
    if K>pos_idx:
#      make all negative value positive
        for idx in range(pos_idx):
            A[idx]=-A[idx]
            K-=1
#       if remain K%2==0, the value sign can be eliminate 
#       if remain K%2==1, one more value must change sign
        if K%2==0:
            pass
#       get the smallest absolute number in A
        else:
#           if exist negatice value in A
            if pos_idx>0:
                if abs(A[pos_idx-1])<A[pos_idx]:
                    A[pos_idx-1]=-A[pos_idx-1]
                else:
                    A[pos_idx]=-A[pos_idx]
#           if no negative value first postive should change sign
            else:
                A[pos_idx]=-A[pos_idx]    
        total=0
        for num in A:
            total+=num
        return total
    else:
        total=0
        for num in A:
            if K>0:
                total-=num
            else:
                total+=num
            K-=1
        return total

    # above code faster
    # clean code
    # i=0
    # A.sort()
    # while A[i]<0 and i<K:
    #     A[i]=-A[i]
    #     i+=1
    # return sum(A)-(K-i)%2*min(A)*2