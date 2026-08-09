class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in numSet:
            cnt = 1
            if n - 1 not in numSet: # check if it's the start of a sequence
                val = (n + 1)
                while val in numSet:
                    cnt += 1
                    val += 1
                res = max(cnt, res)
        return res
            



        
        
        
        

            