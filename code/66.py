from typing import *
def plusOne(digits: List[int]) -> List[int]:
    total=0
    for idx,num in enumerate(digits[::-1]):
        total+=num*(10**idx)
    total+=1
    return [num for num in str(total)]