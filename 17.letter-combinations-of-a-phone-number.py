#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        combos = []

        # use `digits` as a stack

        # While the stack is not empty
        while digits != "":
            # get num_to_char letters
            chars = num_to_chars[digits[0]]
            # pop the first letter off the stack
            digits = digits[1:]

            # if `result` is empty, set combinations equal to COPY of appropriate list and continue
            if not combos:
                combos = chars.copy()
                continue

            # for each value in `combos`, for each value in `num_to_char`, append a string to `combos_next`
            combos_next = []
            for combo in combos:
                for char in chars:
                    combos_next.append(combo + char)

            # set `result` equal to a copy of `result_next`
            combos = combos_next.copy()
        
        return combos
# @lc code=end
