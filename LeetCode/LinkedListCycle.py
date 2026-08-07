# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
from util import time_it


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    @time_it
    def detectCycle(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return -1

        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next:
                return -1
            slow = slow.next
            fast = fast.next.next

        pos = -1
        while head != slow:
            head = head.next
            pos += 1

        return pos

    @time_it
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.detectCycle(head) != -1


if __name__ == "__main__":
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(s.hasCycle(head))  # Output: True
    print(s.detectCycle(head))  # Output: 1