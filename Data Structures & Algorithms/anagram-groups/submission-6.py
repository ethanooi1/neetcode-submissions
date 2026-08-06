class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            ag = ''.join(sorted(word))
            res[ag].append(word)
        return list(res.values())