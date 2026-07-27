class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            r += 1
            res = max(res, len(hashSet))
        return res