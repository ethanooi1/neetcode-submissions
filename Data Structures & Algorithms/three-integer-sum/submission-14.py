class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            j = i+1
            k = len(nums)-1
            while j < k:
                val = a + nums[j] + nums[k]
                if val < 0:
                    j += 1
                elif val > 0:
                    k -= 1
                else:
                    if [a, nums[j], nums[k]] not in res:
                        res.append([a, nums[j], nums[k]])
                    j += 1
        
        return res
            
                
