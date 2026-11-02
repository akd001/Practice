import heapq

from util import time_it


class Solution:

    @time_it
    def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # return heapq.nlargest(k, count.keys(), key=count.get)
        heap = []
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            print(f"Heap after pushing ({c}, {n}): {heap}")
            if len(heap) > k:
                heapq.heappop(heap)

        return [n for c, n in heap]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.top_k_frequent(nums, k))