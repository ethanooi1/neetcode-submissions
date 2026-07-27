class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        countMap = {}
        res = 0

        for r in range(len(s)):
            countMap[s[r]] = countMap.get(s[r], 0) + 1
            while ((r-l+1) - max(countMap.values())) > k:
                countMap[s[l]] = countMap.get(s[l], 0) - 1
                l += 1
            res = max(res, (r-l+1))
        return res
