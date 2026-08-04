class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            sort_s = ''.join(sorted(s))
            seen[sort_s].append(s)
        
        return list(seen.values())
