class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for n in range(len(nums)-1):
            if (nums[n] + nums[n+1]) % 2 == 0:
                return False
        return True