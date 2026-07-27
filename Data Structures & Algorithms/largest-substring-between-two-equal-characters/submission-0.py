class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}

        res = -1

        for i, j in enumerate(s):
            if j in char_index:
                res = max(res, i - char_index[j] - 1)
            else:
                char_index[j] = i
        return res