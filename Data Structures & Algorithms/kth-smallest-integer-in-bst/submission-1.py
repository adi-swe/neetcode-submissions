# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            heapq.heappush(heap, -node.val)
            if len(heap) > k:
                heapq.heappop(heap)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # print(heap)
        return -heap[0]
                
