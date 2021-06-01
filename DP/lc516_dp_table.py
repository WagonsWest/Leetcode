class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        n = len(s)
        for j in range(n-1, -1, -1):
            for i in range(n-j-1):
                ii = i+j+1
                if s[j] == s[ii]:
                    dp[j][ii] = 2 + dp[j+1][ii-1]
                else:
                    dp[j][ii] = max(dp[j][ii-1], dp[j+1][ii])

        return dp[0][n-1]