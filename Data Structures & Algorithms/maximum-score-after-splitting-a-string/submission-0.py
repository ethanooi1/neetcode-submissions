class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            cnt = 0
            for char in s[:i+1]:
                if char == '0':
                    cnt += 1
            for char in s[i+1:]:
                if char == '1':
                    cnt += 1
            res = max(res, cnt)
        return res
            