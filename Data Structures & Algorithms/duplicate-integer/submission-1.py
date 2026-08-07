class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # made a set

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False