class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasher = {}
        for i in nums:
            if i in hasher:
                hasher[i] += 1
            else:
                hasher[i] = 1
        list1 = sorted(hasher, key = hasher.get, reverse = True)
        
        return list1[:k]



            