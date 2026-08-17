class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = set()
        maxlen = 0
        for i in range(len(s)):                
            while s[i] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[i])
            currlen = len(hashset)
            maxlen = max(currlen, maxlen)
        return maxlen
        