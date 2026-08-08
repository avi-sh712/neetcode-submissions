class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in anag:
                anag[key] = []
            anag[key].append(s)
        return list(anag.values())