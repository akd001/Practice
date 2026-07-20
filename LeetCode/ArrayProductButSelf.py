# https://leetcode.com/problems/product-of-array-except-self/

from util import time_it
from typing import List

# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

class Solution:

    @time_it
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allProduct = 1
        numZeros = 0
        for num in nums:
            if num == 0:
                numZeros += 1
                if numZeros > 1:
                    return [0] * len(nums)
                continue
            allProduct *= num
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if numZeros == 0:
                    nums[i] = allProduct // nums[i]
                else:
                    nums[i] = 0
            else:
                nums[i] = allProduct
        return nums
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums))