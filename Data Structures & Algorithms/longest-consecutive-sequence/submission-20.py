class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in numSet: # check if n is the start of a sequence
                val = n + 1
                cnt = 1
                while val in numSet:
                    cnt += 1
                    val += 1
                res = max(res, cnt)
        
        return res
                
                
