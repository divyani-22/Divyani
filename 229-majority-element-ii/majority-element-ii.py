class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        ans = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for i in freq:
            if freq[i] > (len(nums))//3:
                ans.append(i)

        return ans
        