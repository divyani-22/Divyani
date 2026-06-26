class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            a = max(nums[i], a + nums[i])
            maximum = max(maximum, a)
        return maximum
        