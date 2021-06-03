# related to lc523.
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        total = list(accumulate(candiesCount))
        
        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            min_candy = favoriteDay + 1
            max_candy = (favoriteDay + 1) * dailyCap
            prefix_x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            prefix_y2 = total[favoriteType]
            
            ans.append(not(min_candy > prefix_y2 or max_candy < prefix_x2))
        
        return ans
