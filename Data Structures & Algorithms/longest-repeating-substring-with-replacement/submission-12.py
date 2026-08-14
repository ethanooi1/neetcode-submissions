class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        L, R = 0, 0
        mp = {}
        
        while R < len(s):
            mp[s[R]] = mp.get(s[R], 0) + 1 # first add
            if len(s[L:R]) - max(mp.values()) <= k: # check if condition valid
                R += 1 # continue appending
            while len(s[L:R]) - max(mp.values()) > k: # while condition isn't valid
                mp[s[L]] = mp.get(s[L], 0) - 1
                L += 1
            res = max(res, R - L)
        return res

