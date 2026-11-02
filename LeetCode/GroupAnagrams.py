# https://leetcode.com/problems/group-anagrams/

from util import time_it
from typing import List


class Solution:

    class _mem:
        __slots__ = ("data", "_next")

        def __init__(self, data: str) -> None:
            self.data = data
            self._next = None

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        hashMapTail = {}

        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - 97] += 1

            key = tuple(counts)

            if key not in hashMap:
                node = self._mem(s)
                hashMap[key] = node
                hashMapTail[key] = node
            else:
                node = self._mem(s)
                hashMapTail[key]._next = node
                hashMapTail[key] = node

        result = []

        for head in hashMap.values():
            group = []

            while head:
                group.append(head.data)
                head = head._next

            result.append(group)

        return result

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - 97] += 1

            key = tuple(count)
            groups.setdefault(key, []).append(s)

        return list(groups.values())

if __name__ == "__main__":
    s = Solution()
    # print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    # print(s.groupAnagrams([""]))  # Output: [[""]]
    print(s.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))  # Output: [["bdddddddddd"],["bbbbbbbbbbc"]]