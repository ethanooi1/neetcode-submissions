class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            j = i + 1
            k = len(nums)-1
            while j < k:
                if a + nums[j] + nums[k] < 0:
                    j += 1
                elif a + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    if [a, nums[j], nums[k]] not in res:
                        res.append([a, nums[j], nums[k]])
                    j += 1
        
        return res
                