from typing import List
from util import time_it

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]

class Solution:

    @time_it
    def trap(self, height: List[int]) -> int:
        totalWater, left, right = 0, 0, len(height) - 1
        leftMax, rightMax = 0, 0

        ###############################
        while left <= right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    totalWater += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    totalWater += rightMax - height[right]
                right -= 1
        ###############################
            


        # while left <= right:
        #     if leftMax < height[left]:
        #         leftMax = height[left]
        #     if rightMax < height[right]:
        #         rightMax = height[right]
        #     if leftMax < rightMax:
        #         totalWater += leftMax - height[left]
        #         left += 1
        #     else:
        #         totalWater += rightMax - height[right]
        #         right -= 1
            
            # if leftMax < rightMax:
            #     if height[left] < leftMax:
            #         totalWater += leftMax - height[left]
            #     else:
            #         leftMax = height[left]
            #     left += 1
            # else:
            #     if height[right] < rightMax:
            #         totalWater += rightMax - height[right]
            #     else:
            #         rightMax = height[right]
            #     right -= 1
        return totalWater
    
    # @time_it
    # def trap(self, height: List[int]) -> int:
    #     totalWater, left, right = 0, 0, len(height) - 1
    #     leftMax, rightMax = 0, 0
    #     while left < right:
    #         if height[left] < height[right]:
    #             if height[left] >= leftMax:
    #                 leftMax = height[left]
    #             else:
    #                 totalWater += leftMax - height[left]
    #             left += 1
    #         else:
    #             if height[right] >= rightMax:
    #                 rightMax = height[right]
    #             else:
    #                 totalWater += rightMax - height[right]
    #             right -= 1
    #     return totalWater

    @time_it
    def trap2(self, height: List[int]) -> int:
        totalWater, ele, maxHeight = 0, 0, 0
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
        entrapped = False
        for j in range(maxHeight):
            for i in range(len(height)):
                if height[i] - ele > 0:
                    if not entrapped:
                        entrapped = True
                elif entrapped:
                    totalWater += 1
        
        return totalWater

    @time_it
    def trap3(self, height: List[int]) -> int:
        totalWater, ele, maxHeight = 0, 0, 0
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
        entrapped = False
        while ele < maxHeight:
            currWater = 0
            for i in range(len(height)):
                print("> ele, i, height, trapped - ", ele, i, height[i], entrapped)
                if height[i] - ele > 0:
                    if not entrapped:
                        entrapped = True
                        print(">>> entrap start")
                    else:
                        print("<<< entrap end")
                        entrapped = False
                elif height[i] - ele <= 0 and entrapped:
                    currWater += 1
                    print("+++ add water")
                else:
                    print("xxx not entrapped")
            if entrapped:
                totalWater += currWater
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> water stored after elevation - ", ele, totalWater)
            ele += 1
            entrapped = False
        
        return totalWater


if __name__== "__main__":
    solution = Solution()
    print(solution.trap(height))
