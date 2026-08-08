class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        for ch in s:
            if ch in dicts:
                dicts[ch] += 1
            else:
                dicts[ch] = 1
        
        dictt = {}
        for char in t:
            if char in dictt:
                dictt[char] += 1
            else:
                dictt[char] = 1
        
        return dicts == dictt
