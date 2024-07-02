#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [2, 3, 6, 7], 7
        """
        candidates = sorted(candidates)
        stack = [[candidate] for candidate in candidates]
        results = []
        while stack:
            combo = stack.pop()
            s = sum(combo)
            if s > target:
                continue
            if s == target:
                results.append(combo)
                continue
            for candidate in candidates:
                if candidate <= combo[-1]:
                    stack = stack + [combo + [candidate]]
        return results
        
        
        
# @lc code=end

