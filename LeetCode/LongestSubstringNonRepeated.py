# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from util import time_it
from typing import List

s = "abcabcbb"
# s = "pwwkew"
# s = "ab"

class Solution:

    @time_it
    def lengthOfLongestUniqueSubstring(self, s: str) -> int:
        char_hash = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            # logic: if the character is already in the hash and 
            # its index is greater than or equal to left, move left 
            # to the right of that character's last index
            if s[right] in char_hash and char_hash[s[right]] >= left:
                left = char_hash[s[right]] + 1
            char_hash[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length

    @time_it
    def longestSubstringWithKDistinct(self, s: str, k: int) -> int:
        char_hash = {}
        left, max_length = 0, 0
        for right in range(len(s)):
            # logic: if the character is already in the hash, update 
            # its index, otherwise add it to the hash. If the hash size exceeds k,
            # remove the leftmost character from the hash and move left pointer
            char_hash[s[right]] = right
            if len(char_hash) > k:
                least_val = min(char_hash.values())
                for key in char_hash.keys():
                    if char_hash[key] == least_val:
                        del char_hash[key]
                        left = least_val + 1
                        break
            max_length = max(max_length, right - left + 1)
        return max_length



if __name__=="__main__":
    sol = Solution()
    print(sol.lengthOfLongestUniqueSubstring(s))
    print(sol.longestSubstringWithKDistinct(s, 2))