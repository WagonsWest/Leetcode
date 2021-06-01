class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        right = left = 0
        ans = 0
        repeat = 0

        while right<len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
                if window[s[right]] > 1:
                    repeat += 1

            right += 1

            while repeat > 0:
                if window[s[left]] > 1:
                    window[s[left]] -= 1
                    repeat -= 1
                elif window[s[left]] == 1:
                    window[s[left]] -= 1
                left += 1

            if ans < right-left:
                ans = right - left

        return ans