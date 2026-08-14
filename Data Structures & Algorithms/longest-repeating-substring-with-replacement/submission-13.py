class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        L = 0
        mp = {}
        
        for R in range(len(s)):
            mp[s[R]] = mp.get(s[R], 0) + 1 # first add
            while (R - L + 1) - max(mp.values()) > k: # while condition isn't valid
                mp[s[L]] = mp.get(s[L], 0) - 1
                L += 1
            res = max(res, R - L + 1)
        return res

