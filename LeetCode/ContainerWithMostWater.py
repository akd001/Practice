# https://leetcode.com/problems/container-with-most-water/

from typing import List
from util import time_it

# sample
height = [1,8,6,2,5,4,8,3,7]

class Solution:

    @time_it
    def maxArea(self, height: List[int]) -> int:
        x1, x2, maxCap = 0, len(height) -1, 0
       
        while x2 > x1:
            currentCap = min(height[x1], height[x2]) * (x2-x1)
            if currentCap > maxCap:
                maxCap = currentCap
            if height[x1] > height[x2]:
                x2 -= 1
            else:
                x1 += 1
        
        return maxCap

if __name__== "__main__":
    solution = Solution()
    print(solution.maxArea(height))