class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        cntMap = {}
        for r in range(len(s)):
            cntMap[s[r]] = cntMap.get(s[r], 0) + 1
            while (r - l) - max(cntMap.values()) >= k:
                cntMap[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res
                