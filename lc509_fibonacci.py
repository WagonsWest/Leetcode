class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0

        if n==1 or n==2:
            return 1
        prev = 1
        curr = 1
        for i in range(n-2):
            sum = prev + curr
            prev = curr
            curr = sum

        return curr