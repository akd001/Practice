def threeSum(nums):
    """
    Find all unique triplets in the array which gives the sum of zero.

    Args:
        nums: List of integers

    Returns:
        List of lists containing unique triplets that sum to zero
    """
    # Sort the array first
    nums.sort()
    result = []

    # Iterate through each element as the first element of triplet
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Use two pointers to find pairs that sum to -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1

            elif current_sum < 0:
                # Sum is too small, move left pointer to increase sum
                left += 1
            else:
                # Sum is too large, move right pointer to decrease sum
                right -= 1

    return result

# Test the function
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {nums1}")
    print(f"Output: {threeSum(nums1)}")

    # Test case 2
    nums2 = [0, 1, 1]
    print(f"Input: {nums2}")
    print(f"Output: {threeSum(nums2)}")

    # Test case 3
    nums3 = [0, 0, 0]
    print(f"Input: {nums3}")
    print(f"Output: {threeSum(nums3)}")