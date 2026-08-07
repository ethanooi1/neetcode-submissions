class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        area = 0
        res = 0
        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            res = max(area, res)
            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return res
            
            
            
        