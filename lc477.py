class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            #(x & 1) is (the last bit of x) AND (1)
            #check how many bits at ith position is 1
            #hamming distance of ith bit is c*(n-c)
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
        