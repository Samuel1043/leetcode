class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_cnt=0
        l_cnt=0
        ans=0
        for char in s:
            if char=='R':
                r_cnt+=1
            elif char=='L':
                l_cnt+=1
            if r_cnt==l_cnt:
                r_cnt=0
                l_cnt=0
                ans+=1
        return ans