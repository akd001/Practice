# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from util import time_it
from typing import List

# nums = [2,7,11,15]
# k = 9

# nums = [2, 25, 75]
# k = 100

nums = [3,24,50,79,88,150,345]
k = 200

# [5, 10, 20, 30, 50, 100, 150, 200, 300, 400, 500]
# 305

# 5, 500


class Solution:

    @time_it
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        # try 1
        # while left < right:
        #     current_sum = numbers[left] + numbers[right]
        #     if current_sum == target:
        #         return [left + 1, right + 1]  # Return 1-based indices
        #     elif current_sum < target:
        #         left += 1
        #     else:
        #         right -= 1
        #######

        # try 2
        divFactorLeft = divFactorRight = 2
        while left < right:
            print(f">>> Left: {left}, Right: {right}")
            current_sum = numbers[left] + numbers[right]
            print(f"Current Sum: {current_sum}, Numbers: {numbers[left]}, {numbers[right]}")
            if current_sum == target:
                return [left + 1, right + 1] 
            elif current_sum < target:
                print(">>> Moving Left Pointer")
                leftTemp = left + int((right - left) / divFactorLeft)
                print(f">>> Left Temp: {leftTemp}, Right: {right}")
                while (numbers[leftTemp] > target - numbers[right]) and (leftTemp < right) and divFactorLeft < (right - left):
                    divFactorLeft += 1
                    leftTemp = left + int((right - left) / divFactorLeft)
                    print(f">>> Left Temp: {leftTemp}, DivFactor: {divFactorLeft}")
                if numbers[leftTemp] <= target - numbers[right]:
                    left = leftTemp
            else:
                print(">>> Moving Right Pointer")
                rightTemp = right - int((right - left) / divFactorRight)
                while (numbers[rightTemp] < target - numbers[left]) and (left < rightTemp) and divFactorRight < (right - left):
                    divFactorRight += 1
                    rightTemp = right - int((right - left) / divFactorRight)
                    print(f">>> Right Temp: {rightTemp}, DivFactor: {divFactorRight}")
                if numbers[rightTemp] >= target - numbers[left]:
                    right = rightTemp
                
            print(f"<<< Left: {left}, Right: {right}")
            if right == 3 and left == 2:
                break
            
        #######

        return []  # If no solution is found


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums, k))