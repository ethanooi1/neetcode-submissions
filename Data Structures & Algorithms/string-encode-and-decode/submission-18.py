class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ''
        for s in strs:
            length = len(s)
            word += str(length) + '#' + s
        return word

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res
