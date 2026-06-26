class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans


    

      
        #ans = [0] * len(nums)
        #pos = 0
        #neg = 1
        #for i in nums:
        #    if i > 0:
        #        ans[pos] = i
        #        pos += 2
        #    else:
        #        ans[neg] = i
        #        neg += 2

        #return ans'''

        