class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for n in nums:
            if n == 0:
                cnt = 0
            else:
                cnt += 1
            res = max(cnt, res)
        return res