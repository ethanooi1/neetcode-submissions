class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = [0] * 26
        for c in s1:
            cnt[ord(c) - ord('a')] += 1
        
        L = 0
        R = len(s1)
        while R <= len(s2):
            cnt2 = [0] * 26
            for c in s2[L:R]:
                cnt2[ord(c) - ord('a')] += 1
            if cnt2 == cnt:
                return True
            L += 1
            R += 1

        return False
