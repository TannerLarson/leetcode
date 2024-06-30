#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        assert len(symbols) == len(values)
        
        # Keep track of the max value
        i = 0
        
        while num != 0:
            # Loop through numerals (starting at `i`) until we get to a number we can subtract
            while values[i] > num:
                i += 1
            # Subtract the numeral
            num -= values[i]
            # Add the symbol of the numeral to `roman`
            roman += symbols[i]
        
        return roman
        
        
            
# @lc code=end

