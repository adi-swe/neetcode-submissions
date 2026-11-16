# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        r = root

        while r:
            if p.val > r.val and q.val > r.val:
                r = r.right
            elif p.val < r.val and q.val < r.val:
                r = r.left
            else:
                return r