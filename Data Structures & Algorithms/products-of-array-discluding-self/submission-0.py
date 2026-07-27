class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sub = []
        output = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            sub.append(temp)
        for n in sub:
            agg = 1
            for num in n:
                agg = agg * num
            output.append(agg)
        return output