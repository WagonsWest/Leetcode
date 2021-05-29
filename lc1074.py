import collections

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        def subarraySum(nums, k):
            mp = collections.Counter([0])
            count = pre = 0
            # O(n)
            for x in nums:
                pre += x
                if pre - k in mp:
                # the new x equals to k; at least count += 1 for the x itself
                # if mp[pre-k]>1, it means there exists a segment of pre_list that sums to 0
                # |a| 0 |x|; so |0|+|x| can create a new matrix.
                    count += mp[pre - k]
                mp[pre] += 1
            return count
        
        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 枚举上边界
        # O(m)
        for i in range(m):
            total = [0] * n
            # 枚举下边界
            # O(m)
            for j in range(i, m):
                # O(n)
                for c in range(n):
                    # 更新每列的元素和
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)
        
        # O(m^2 * n)
        return ans