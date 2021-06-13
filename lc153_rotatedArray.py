class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0 
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)/2
            if nums[left] < nums[mid] and nums[mid] < nums[right]:
                return nums[left]
            elif nums[left] <= nums[mid] and nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]