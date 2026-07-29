class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            w = ''.join(sorted(word))
            seen[w].append(word)
        return list(seen.values())