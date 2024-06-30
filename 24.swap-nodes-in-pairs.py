#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse the linked list
        """
        When editing a linked list, you need to know about three nodes. The node you left off at, and the two nodes you want to edit
        """
        
        node = head
        prev = new_head = None
        
        while node and node.next:
            """ [a, b, c, d]
            [a, head -> b -> c -> d -> None]
            
            [a, head -> c -> d -> None]
             b ---^
             
            [b -> a, head -> c -> d -> None]
            
            [new_head -> b -> a, ~~head~~ -> c -> d -> None]
            
            [new_head -> b -> a -> c -> d -> None]
            
            [new_head -> b -> a -> c -> None]
                                   d ---^

            [new_head -> b -> a -> c -> None]
                              d ---^
                              
            [new_head -> b -> a -> d -> c -> None]
            """
            node_prev = node #           [1, 2, 3, 4]  [3, 4]
            node = node.next #           [2, 3, 4]     [4]
            node_prev.next = node.next # [1, 3, 4]     [3]
            node.next = node_prev #      [2, 1, 3, 4]  [4, 3]
            
            if prev:
                prev.next = node
            else:
                new_head = node
            
            prev = node.next
            node = node.next.next #     [3, 4]
            
        return new_head or head
# @lc code=end

