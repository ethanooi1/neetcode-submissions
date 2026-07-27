class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                length = 1
                x = n
                while x + 1 in nums:
                    length += 1
                    x += 1
                res = max(res, length)
        return res

            