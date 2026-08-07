# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from util import time_it
from typing import List

# s = "abcabcbb"
s = "pwwkew"

class Solution:
    @time_it
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, left = 0, 0
        charMap = {}
        for i in range(len(s)):
            print("\n> s[i], charMap - ", s[i], charMap)
            if charMap.get(s[i]):
                left = charMap[s[i]] + 1
                charMap[s[i]] = i
                print(">>> move left to - ", left)
            else:
                charMap[s[i]] = i
                print(">>> add char - ", s[i])
            if i - left >= maxLen:
                maxLen = i - left
            print("< charMap - ", charMap)
            print("< left, maxLen -", left, maxLen)
        return maxLen


if __name__=="__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))