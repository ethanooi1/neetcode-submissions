class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        L = 0
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        for c in s1:
            s1_arr[ord(c) - ord('a')] += 1 # creates freq table of s1

        for R in range(len(s2)):
            s2_arr[ord(s2[R]) - ord('a')] += 1
            if R - L >= len(s1):
                s2_arr[ord(s2[L]) - ord('a')] -= 1
                L += 1
            if s1_arr == s2_arr:
                return True
        return False

            
                
