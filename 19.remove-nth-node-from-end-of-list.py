#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        # Find length of linked list
        node = head
        length = 1
        while (node:=node.next) is not None:
            length += 1
            
        if n == length:
            return head.next
            
        # Find n - 1 and n + 1
        node = head
        i = 0
        left = right = None
        while True:
            if i == length - n - 1:
                left = node
            if i == length - n + 1:
                right = node
            
            if node is None:
                break
            node = node.next
            i += 1
        
        # Set n - 1 next to n + 1
        if not right:
            left.next = None
            return head
        left.next = right
        return head
# @lc code=end

