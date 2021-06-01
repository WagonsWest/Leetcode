class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        slow = 0
        fast = len(numbers)-1
        while slow < fast:
            if numbers[slow] + numbers[fast] == target:
                return [slow+1, fast+1]
            elif numbers[slow] + numbers[fast] < target:
                slow += 1
            elif numbers[slow] + numbers[fast] > target:
                fast -= 1