# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        layer = 0
        def zz(root, ans, layer):
            if root != None:
                if len(ans) == layer:
                    ans.append([])
                ans[layer].append(root.val)
                zz(root.left, ans, layer+1)
                zz(root.right, ans, layer+1)

        zz(root, ans, layer)
        for i in range(len(ans)):
            if i%2 != 0:
                ans[i].reverse()
        return ans
