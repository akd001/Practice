from util import time_it


class Solution:
    @time_it
    def removeDuplicates0(self, nums: list[int]) -> int:
        cur_num = 0
        cur_num_count = 0
        count = 0
        count_removed = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            if cur_num_count == 1 and cur_num == num:
                cur_num_count += 1
                count += 1
                i += 1
            elif cur_num_count == 2 and cur_num == num:
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                count_removed += 1
            else:
                cur_num = num
                cur_num_count = 1
                count += 1
                i += 1
            
            if count + count_removed == len(nums):
                break
        return count


    def removeDuplicates(self, nums: list[int]) -> int:
        cur_num = 0
        cur_num_count = 0
        count = 0
        count_removed = 0
        i = 0
        index_removed = set()
        while i < len(nums):
            num = nums[i]
            if cur_num_count == 1 and cur_num == num:
                cur_num_count += 1
                count += 1
                i += 1
            elif cur_num_count == 2 and cur_num == num:
                i += 1
                count_removed += 1
                index_removed.add(i)
            else:
                cur_num = num
                cur_num_count = 1
                count += 1
                i += 1
            
            if count + count_removed == len(nums):
                break
        # print(f"index_removed: {index_removed}")

        # pop logic 1
        # for index in sorted(index_removed, reverse=True):
        #     nums.pop(index-1)

        # pop logic 2
        replace_set = set()
        diff = len(nums) - count
        i = len(nums) - 1
        while i >= 0 and len(index_removed) > 0:
            print(f"i: {i}, diff: {diff}, index_removed: {index_removed}")
            if (i - diff) not in index_removed:
                print(f"Adding nums[{i - diff}] = {nums[i - diff]} to replace_set")
                replace_set.add(nums[i - diff])
                nums[i - diff] = nums[i]
            else:
                print(f"Removing index {i - diff} from index_removed")
                index_removed.remove(i - diff)
                print(f"Adding nums[{i - diff}] = {nums[i - diff]} to replace_set")
                nums[i - diff] = nums[i]
            i -= 1
        print("nums after pop logic 2:", nums, "replace_set:", replace_set, "diff:", diff)
        while diff > 0 and len(replace_set) > 0:
            nums[count + diff - 1] = replace_set.pop()
            diff -= 1
        
        print(f"Final nums: {nums[:count]}")
        return count


if __name__ == "__main__":
    sol = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    result = sol.removeDuplicates(nums)
    print(result, nums[:result])