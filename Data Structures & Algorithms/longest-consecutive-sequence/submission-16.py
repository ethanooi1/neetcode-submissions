class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        cnt = 1
        res = 0
        val = 0 
        for num in nums:
            if num-1 not in nums: # check if start of sequence
                val = (num + 1)
                while val in nums: # if the next consecutive exists in our set, add to count
                    cnt += 1
                    val += 1
                res = max(res, cnt) # if the next consecutive doesn't exist, that's the end of that start, update res
                cnt = 1
                

        return res
                