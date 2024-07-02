#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
"""
Iterate backwards

1. what indexes could get to 5?
2. What indexes could get to those valid indexes?
3. Keep going until 

"""
# [9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]
# [0, 8, 12, 19]
# 0, 7, 11, 19
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        nums.reverse()
        stack = [[0]]
        shortest_paths = [None for _ in range(len(nums))]
        shortest_paths[0] = [0]
        while stack:
            print(f"{stack}\n{shortest_paths}\n")
            jumps = stack.pop()
            jump_prev = jumps[-1]
            
            jump_next = jump_prev + 1
            while jump_next < len(nums) and jump_next <= jump_prev + nums[jump_prev]:
                # Make sure we can actually get to the next number
                if jump_next - nums[jump_next] > jump_prev:
                    jump_next += 1
                    continue
                
                if not shortest_paths[jump_next] or len(jumps) + 1 < len(shortest_paths[jump_next]):
                    shortest_paths[jump_next] = jumps + [jump_next]
                    stack += [jumps + [jump_next]]
                jump_next += 1
        print(shortest_paths[len(nums) - 1])
        return len(shortest_paths[len(nums) - 1]) - 1
            
        # stack = [[0]]
        # shortest_paths = {0: [0]}
        
        # while stack:
        #     # print(stack)
        #     # print(shortest_paths)
        #     # print()
        #     jumps = stack.pop()
        #     jump_prev = jumps[-1]
            
        #     # Add next steps to stack
        #     jump_next = jump_prev + 1
        #     while jump_next < len(nums) and jump_next <= jump_prev + nums[jump_prev]:
        #         jumps_next = jumps + [jump_next]
        #         # If next value already in shortest_jumps
        #         if jump_next in shortest_paths:
        #             # Update shortest_jumps
        #             # Don't add to stack because we've already covered it
        #             if len(jumps_next) < len(shortest_paths[jump_next]):
        #                 shortest_paths[jump_next] = jumps_next.copy()
        #                 stack = stack + [jumps_next]
        #         # Otherwise, add to stack
        #         else:
        #             shortest_paths[jump_next] = jumps_next.copy()
        #             stack = stack + [jumps_next]
        #         jump_next += 1

        
        # print(shortest_paths[len(nums) - 1])
        # return len(shortest_paths[len(nums) - 1]) - 1
            
# @lc code=end

