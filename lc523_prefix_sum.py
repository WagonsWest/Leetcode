# 哈希表+前缀和
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False

        remainder = 0
        prefix_list = {}
        for i in range(n):
            remainder = (remainder+nums[i])%k
            if remainder == 0 and i >= 1:
                return True
            elif remainder in prefix_list:
                if i-prefix_list[remainder] >= 2:
                    return True
            else:
                prefix_list[remainder] = i

        return False