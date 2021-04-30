# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            cond=isBadVersion(mid)
            if cond:
                end=mid-1
            else:
                start=mid+1
        return start
