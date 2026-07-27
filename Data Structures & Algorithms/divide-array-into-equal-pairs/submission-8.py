class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1
        for i in res.values():
            if not i % 2 == 0:
                return False
        return True