class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        if len(s) == 0:
            return 0
        L, res = 0, 1

        for R in range(len(s)):
            while s[R] in charSet:
                
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            res = max(len(charSet), res)
        
        return res
