class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ls = sorted(s)
        t_ls = sorted(t)
        if s_ls == t_ls:
            return True
        return False