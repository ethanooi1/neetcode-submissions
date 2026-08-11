class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cnt = 0
        L = 0
        seen = set()

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                cnt -= 1
                L += 1
            seen.add(s[R])
            cnt += 1
            res = max(cnt, res)
        return res
            
