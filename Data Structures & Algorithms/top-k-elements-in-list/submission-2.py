class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasher = {}
        for i in nums:
            hasher[i] = hasher.get(i, 0) + 1
        list1 = sorted(hasher, key = hasher.get)
        return list1[len(list1) - k: len(list1)]



            