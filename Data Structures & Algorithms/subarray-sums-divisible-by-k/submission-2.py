from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hasher = defaultdict(int)
        hasher[0] = 1
        count = 0
        for x in nums:
            prefix_sum += x
            rem = prefix_sum % k
            if rem in hasher:
                count += hasher[rem]
            hasher[rem] +=1
        return count