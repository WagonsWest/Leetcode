# BFS
class Solution:
    def levelOrder(self, root: TreeNode):
        from collections import deque
        queue = deque()
        result = []
        if not root:
            return []
        queue.append(root)
        while queue:
            current_level_size = len(queue)
            current_level = []
            for _ in range(current_level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

# another method:
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def layerSearch(node: TreeNode, layer):
            if node != None:
                if len(res) == layer:
                    res.append([])
                res[layer].append(node.val)
                layerSearch(node.left, layer+1)
                layerSearch(node.right, layer+1)

        layerSearch(root, 0)
        return res