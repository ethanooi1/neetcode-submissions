class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w, x = sorted(nums)[-2:]
        y, z = sorted(nums)[:2]
        return (w * x) - (y * z)
            