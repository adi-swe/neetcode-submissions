class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, maxarea = 0, 0
        left, right = 0, len(heights) - 1

        while(left < right):
            width = right - left
            area = min(heights[left], heights[right]) * width
            maxarea = max(maxarea, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxarea
        