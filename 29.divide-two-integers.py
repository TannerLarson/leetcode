#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend >= 0) != (divisor > 0)
        
        numerator, denominator = abs(dividend), abs(divisor)
        
        if denominator == 1:
            return 0 - numerator if is_negative else numerator
        
        result = 0
        while numerator >= denominator:
            result += 1
            
            numerator -= denominator
            
        print(result)
        if result > 2**31 - 1:
            result = 2**31 - 1
        print(result)
        
        return 0 - result if is_negative else result
        
# @lc code=end

