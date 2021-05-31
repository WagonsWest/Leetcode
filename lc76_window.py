#滑动窗口 注意边际条件！！！
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {chr: t.count(chr) for chr in set(t)}
        missing = len(t)
        right = left = 0
        best_cur = ''
        best_len = len(s)

        if len(s) < missing:
            return ''

        while right<len(s):
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    missing -= 1
            right += 1

            while missing == 0:
                if len(t) == 1:
                    return t
                if best_len >= right-left:
                    best_len = right-left
                    best_cur = s[left:right]

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        missing += 1
                left += 1

        return best_cur