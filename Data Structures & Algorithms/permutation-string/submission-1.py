class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        new_s1 = ''.join(sorted(s1))
        
        L = 0
        R = len(new_s1)
        while R <= len(s2):
            if ''.join(sorted(s2[L:R])) == new_s1:
                return True
            R += 1
            L += 1
        return False