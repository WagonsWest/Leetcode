# related to lc438
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = {chr: s1.count(chr) for chr in set(s1)}
        missing = len(s1)
        right = left = 0
        ans = False

        if len(s2) < missing:
            return False

        while right<len(s2):
            if s2[right] in need:
                need[s2[right]] -= 1
                if need[s2[right]] >= 0:
                    missing -= 1
            right += 1

            if right-left == len(s1):
                if missing == 0:
                    return True
                else:
                    if s2[left] in need:
                        need[s2[left]] += 1
                        if need[s2[left]] > 0:
                            missing += 1
                left += 1

        return False