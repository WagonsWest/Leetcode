class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack, node = [], root

        if not root: return [] # 基本情况直接返回
        while stack or node:
            while node:
                stack.append(node) # 先把节点放到栈里面
                node = node.left # 看它有没有左分支，如果有，这个while循环会走到底
            node = stack.pop() # 把根pop出来，把他的值放到list里面
            res.append(node.val) 
            node = node.right # 看他有没有右分支，然后重复
        return res