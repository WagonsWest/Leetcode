class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        f = [1] * (n)

        for i in range(n):
            for j in range(i):
                if nums[j]  < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        
        res = 0
        for i in range(n):
            res = max(res, f[i])
        return res
