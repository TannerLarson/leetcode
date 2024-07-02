#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List

class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        stack = [([candidate]) for candidate in candidates]
        # [1, 1, 2, 5, 6, 7, 10]
        
        while stack:
            print(stack)
            combo = stack.pop()
            s = sum(combo)
            if s > target:
                continue
            if s == target:
                results.append(combo)
                continue
            for candidate in candidates[:-len(combo)]:
                if candidate <= combo[-1]:
                    print(f"{combo} {candidate}")
                    stack += [combo + [candidate]]
               
        results = {tuple(result) for result in results}
        return results
                
        
# @lc code=end

