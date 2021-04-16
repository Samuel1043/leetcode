from typing import List
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        ans=[]
        cnt=0
        edge=0
        row=r0
        col=c0

        def append_ans(r,c,cur_edge,direction):
            while cur_edge>0:
                if 0<=r<R and 0<=c<C:
                    ans.append([r,c])
                r,c=r+direction[0],c+direction[1]
                cur_edge-=1
            return r,c
        while True:

            if len(ans)==R*C:
                return ans

            if cnt%2==0:
                edge+=1


            if cnt%4==0:
                row,col=append_ans(row,col,edge,(0,1))
                # down
            elif cnt%4==1:
                row,col=append_ans(row,col,edge,((1,0)))
                # left
            elif cnt%4==2:
                row,col=append_ans(row,col,edge,(0,-1))
                # up
            else:
                row,col=append_ans(row,col,edge,(-1,0))

            cnt+=1
        return ans


if __name__ =='__main__':
    sol=Solution()
    print(sol.spiralMatrixIII(R = 1, C = 4, r0 = 0, c0 = 0))