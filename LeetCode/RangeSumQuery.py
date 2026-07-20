# Link - https://leetcode.com/problems/range-sum-query-immutable/


from typing import List
import util


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.numsSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.numsSum[i + 1] = self.numsSum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.numsSum[right + 1] - self.numsSum[left]
        

if __name__ == "__main__":
    with util.Timer() as t:
        solution = NumArray([-2, 0, 3, -5, 2, -1])
        print(solution.sumRange(0, 2))
        print(f"Time taken: {t.elapsed:.6f} seconds")
