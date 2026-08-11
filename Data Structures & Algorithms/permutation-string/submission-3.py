class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = [0] * 26
        for c in s1:
            cnt[ord(c) - ord('a')] += 1
        
        L = 0
        cnt2 = [0] * 26
        for R in range(len(s2)):
            if R - L < len(s1):
                cnt2[ord(s2[R]) - ord('a')] += 1
                if cnt2 == cnt:
                    return True
            else:
                cnt2[ord(s2[L]) - ord('a')] -= 1
                cnt2[ord(s2[R]) - ord('a')] += 1
                if cnt2 == cnt:
                    return True
                L += 1

        return False
