from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)# Auto creates this dictionary's keys to a list[]
        for s in strs:
            key = tuple(sorted(s))
            anag[key].append(s)
        return list(anag.values())