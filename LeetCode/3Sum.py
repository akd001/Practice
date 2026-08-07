# https://leetcode.com/problems/3sum/description/


from os import wait
import time

from util import time_it


nums = [-1, 0, 1, 2, -1, -4]
k = 0


class Solution:
    @time_it
    def threeSum(self, nums: list[int], k: int = 0) -> list[list[int]]:
        nums.sort()  # Sort the array to use two-pointer technique
        print(f"Sorted nums: {nums}")
        result = []
        result_set = set()  # To avoid duplicates
        left, center, right = 0, 0, len(nums) - 1

        while left < right:
            print(f"> Checking pair: nums[left]={nums[left]}, nums[right]={nums[right]}")
            print(f">   Current left index: {left}, right index: {right}")
            if nums[left] + nums[right] > k:
                right -= 1
                continue
            elif nums[left] + nums[right] < k:
                center = left + 1
                target = k - (nums[left] + nums[right])
                while center < right:
                    print(f">      Checking center index: {center}, nums[center]={nums[center]}, target={target}")
                    if nums[center] == target:
                        print(f"Found triplet: {nums[left]}, {nums[center]}, {nums[right]}")
                        triplet = f"{nums[left]}_{nums[center]}_{nums[right]}"
                        if triplet not in result_set:
                            result.append([nums[left], nums[center], nums[right]])
                            result_set.add(triplet)
                        # result.append([nums[left], nums[center], nums[right]])
                        break
                    elif nums[center] < target:
                        print(f">      Checking center index: {center}, nums[center]={nums[center]}, target={target}")
                        center += 1
                    else:
                        left += 1
                        break
            print(f">   result so far: {result}")
            print(f">   result_set so far: {result_set}")
            print(f">   Ending left index: {left}, right index: {right}")
            time.sleep(1)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums, k))



20 + 3.6 = 23.6

10 + 1.8 = 11.8