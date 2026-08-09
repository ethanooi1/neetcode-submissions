class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        res = 0
        L = 0
        maxf = 0
        for R in range(len(s)):
            hashMap[s[R]] = hashMap.get(s[R], 0) + 1
            maxf = max(maxf, hashMap[s[R]])

            while (R - L + 1) - maxf > k:
                hashMap[s[L]] = hashMap.get(s[L], 0) - 1
                L += 1
                
            res = max(R - L + 1, res)
            
        return res
