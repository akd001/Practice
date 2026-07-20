# Link - https://leetcode.com/problems/contiguous-array/description/

from util import time_it
from typing import List

# Sample Input -
nums = [0,1,1,1,1,1,0,0,0,]
# nums = [0,1,0]

class Solution:
    @time_it
    def findMaxLength(self, nums: List[int]) -> int:
        currentCount = maxLength = 0
        currentCountIndicesMap = {
                    0: {
                        first_index := -1,
                        maxLength := 0
                    }
                } #{0: [-1]}  # Initialize with -1 to handle the case when the subarray starts from index 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentCount += 1
            else:
                currentCount -= 1
            print(">>> ", currentCount, currentCountIndicesMap)
            if currentCount in currentCountIndicesMap:
                maxLength = max(maxLength, i - currentCountIndicesMap[currentCount].first_index)
                currentCountIndicesMap[currentCount].maxLength = maxLength
            else:
                currentCountIndicesMap[currentCount] = {
                    first_index := i,
                    maxLength := 0
                }
            # print(f"Index: {i}, Current Count: {currentCount}, Indices Map: {currentCountIndicesMap}")
        if currentCount == 0:
            return len(nums)
        else:
            return maxLength
        # for count, indices in currentCountIndicesMap.items():
        #     # print(f"Count: {count}, Indices: {indices}")
        #     if len(indices) > 1:
        #         # print(f"MaxLength: {maxLength}, Count: {count}, Length: {indices[-1] - indices[0]}")
        #         maxLength = max(maxLength, indices[-1] - indices[0])
        # return maxLength
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxLength(nums))
