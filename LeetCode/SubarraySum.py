# https://leetcode.com/problems/subarray-sum-equals-k/description/

from util import time_it
from typing import List

# nums = [1, 2, 3]
nums = [1, 2, 3, -2, 1, 1]
# nums = [1, 2, 3, 4, 5, 1, 1, 1, 3, 2, 1]
k = 3

class Solution:

    @time_it
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currentSum = 0
        sumFrequencyMap = {0: 1}  # Initialize with 0 sum frequency

        for num in nums:
            currentSum += num
            if (currentSum - k) in sumFrequencyMap:
                count += sumFrequencyMap[currentSum - k]
            sumFrequencyMap[currentSum] = sumFrequencyMap.get(currentSum, 0) + 1

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum(nums, k))


# 000 sumFreqMap = {0: 1}             nums = [1, 2, 3]            k = 3
##loops -
# 001> sumFreqMap = {0: 1}             num = 1        currentSum = 0          count = 0
# 001                                                 currentSum = 1
# 001 1 - 3 = -2 not in sumFreqMap
# 001< sumFreqMap = {0: 1, 1: 1}      count = 0
# 002> sumFreqMap = {0: 1, 1: 1}      num = 2        currentSum = 1          count = 0
# 002                                                 currentSum = 3
# 002 3 - 3 = 0 in sumFreqMap         count = 1
# 002< sumFreqMap = {0: 1, 1: 1, 3: 1}      count = 1
# 003> sumFreqMap = {0: 1, 1: 1, 3: 1}      num = 3        currentSum = 3          count = 1
# 003                                                 currentSum = 6
# 003 6 - 3 = 3 in sumFreqMap         count = 2
# 003< sumFreqMap = {0: 1, 1: 1, 3: 1, 6: 1}      count = 2

