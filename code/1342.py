class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        step=0
        while num>0:
            if (num & 1 == 1) and num!=1:
                step+=2  
            elif (num & 1 == 1) and num==1:
                step+=1
            else:
                step+=1
            num=num >> 1
        
        return step


if __name__ =='__main__':
    sol=Solution()
    print(sol.numberOfSteps(0))