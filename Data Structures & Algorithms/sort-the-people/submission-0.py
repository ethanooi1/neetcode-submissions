class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = {}
        for i, j in zip(heights, names):
            res[i] = j
        
        ans = []
        for h in sorted(heights, reverse=True):
            ans.append(res[h])
        return ans