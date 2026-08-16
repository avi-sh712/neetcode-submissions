class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        max_volume = 0
        if len(heights) <= 1:
            return 0
        for i in range(len(heights)):
            curr_vol = (e-s) * min(heights[s], heights[e])
            while s < e:
                curr_vol = (e-s) * min(heights[s], heights[e])
                if heights[s] <= heights[e]:
                    s += 1
                elif heights[s] > heights[e]:
                    e -= 1
                
                max_volume = max(max_volume, curr_vol)

            
        return max_volume
               