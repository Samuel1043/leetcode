import heapq
from typing import *
class Solution:
    # def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:      
    #     for i in range(len(boxTypes)):
    #         boxTypes[i]=[-boxTypes[i][1],boxTypes[i][0]]
        
    #     heapq.heapify(boxTypes)
    #     total_units=0
    #     while boxTypes and truckSize>0:
    #         units,boxes=heapq.heappop(boxTypes)

    #         units=-units
    #         truckSize-=boxes
            
    #         if truckSize<0:
    #             total_units+=((truckSize+boxes)*units)
    #         else:
    #             total_units+=(boxes*units)
    #     return total_units
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         bucket sort
#       max number of unit per box
        N=1000
        bucket=[0 for _ in range(N)]
        for box in boxTypes:
            bucket[box[1]-1]+=box[0]
        res=0
        while N>0 and truckSize>0:
            cur_boxes=min(truckSize,bucket[N-1])
            res+=cur_boxes*(N)
            truckSize-=cur_boxes
            N-=1
            
        return res

if __name__ =='__main__':
    sol=Solution()
    print(sol.maximumUnits([[4,3],[8,2],[2,10]],10))