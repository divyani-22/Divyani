class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        c=[]
        for i in nums:
            c.append(i*i)
        c.sort()    
        return c
        