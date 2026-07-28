class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = Counter()
        for word in words:
            res.update(word)
        return all(v % len(words) == 0 for v in res.values())