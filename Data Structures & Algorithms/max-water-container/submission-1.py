class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # Brute Force 
        # max_area = 0
        # for i in range(0,len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j-i)
        #         if area > max_area:
        #             max_area = area

        res = 0
        l = 0 
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        