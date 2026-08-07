class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxL, maxR = height[L], height[R]
        sum = 0
        
        while L < R:
            if maxL <= maxR:
                L += 1
                maxL = max(height[L], maxL)
                sum += maxL - height[L]
            else:
                R -= 1
                maxR = max(height[R], maxR)
                sum += maxR - height[R]
        return sum