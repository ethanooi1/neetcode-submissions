class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L = 0
        R = len(height)-1
        maxL, maxR = height[L], height[R]

        while L < R:
            maxL, maxR = max(height[L], maxL), max(height[R], maxR)
            if maxL <= maxR:
                res += (maxL - height[L])
                L += 1
            else:
                res += (maxR - height[R])
                R -= 1
            
        return res




