class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[None]*len(piles) for i in range(len(piles))]

        for i in range(len(piles)):
            for j in range(len(piles)):
                dp[i][j] = [0, 0]

        for i in range(len(piles)):
            dp[i][i] = [piles[i], 0]

        for l in range(1, len(piles)):
            for i in range(len(piles)-l):
                j = l+i
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left>right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]

        ans = dp[0][len(piles)-1]
        return True if ans[0]>ans[1] else False

piles = [5,3,4,5]
print(Solution.stoneGame(Solution, piles))
