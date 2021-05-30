#递归
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = dict()
        def dp(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 0

            if n < 0:
                return -1

            remain = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                #每一轮取最小值
                remain = min(remain, 1 + subproblem)
        
            #若有实数解，返回实数解；若无返回-1
            memo[n] = remain if remain != float('INF') else -1
            return memo[n]

        return dp(amount)

#迭代
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i-coin < 0: continue
                dp[i] = min(dp[i], 1+dp[i-coin])

        return dp[amount] if dp[amount]!=amount+1 else -1
