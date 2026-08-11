class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 0
        L = 0
        for R in range(len(s)):
            mp[s[R]] = mp.get(s[R], 0) + 1
            if len(s[L:R+1]) - max(mp.values()) > k:
                mp[s[L]] = mp.get(s[L], 0) - 1
                L += 1
            res = max(res, R - L+1)
        return res