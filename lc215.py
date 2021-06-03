# library sorted()
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new_nums = sorted(nums)
        n = len(nums)

        return new_nums[n-k]

# heapSort
