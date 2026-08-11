# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque()
        queue.append(root)
        res = list()


        while queue:
            qlen = len(queue)
            level = list()

            for i in range(qlen):
                node = queue.popleft()

                if node:
                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level:
                res.append(level)

        return res
            

        