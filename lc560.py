import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = collections.Counter([0])
        count = pre = 0
        # O(n)
        for x in nums:
            pre += x
            if pre - k in mp:
            # the new x equals to k; at least count += 1 for the x itself
            # if mp[pre-k]>1, it means there exists a segment of pre_list that sums to 0
            # |a| 0 |x|; so |0|+|x| can create a new matrix.
                count += mp[pre - k]
            mp[pre] += 1
        return count