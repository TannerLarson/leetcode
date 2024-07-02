#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        1
        11
        21
        1211
        111221
        312211
        
        1. Increment i until we get to a char that isn't the first char
        2. Append a new encoded string
        """
        say = "1"
        for _ in range(1, n):
            say = self.encode(say)
        return say
        
    def encode(self, s: str) -> str:
        encoded = ""
        i = 0
        while i < len(s):
            num = s[i]
            count = 0
            while i < len(s) and s[i] == num:
                i += 1
                count += 1
            encoded += str(count) + num
        return encoded
            
        
# @lc code=end

