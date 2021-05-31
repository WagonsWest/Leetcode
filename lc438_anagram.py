# related to lc76
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = {chr: p.count(chr) for chr in set(p)}
        missing = len(p)
        right = left = 0
        ans = []

        if len(s) < missing:
            return []

        while right<len(s):
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    missing -= 1
            right += 1

            if right-left == len(p)+1:
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        missing += 1
                left += 1

            if missing == 0:
                ans.append(left)

        return ans