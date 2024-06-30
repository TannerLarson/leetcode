#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Start with a single pair of parentheses
        # ()
        
        # Add the possible combinations for a second pair
        # {}()
        # ({})
        # (){}
        
        # Add the possible combinations for a third pair
        # {}()()
        # ({})()
        # ()({})
        # ()(){}
        
        # {}(())
        # ({}())
        # (({}))
        # ((){})
        # (()){}
        if n == 0:
            return []
        
        results = ["()"]
        # Add parentheses n times
        for _ in range(1, n):
            # Loop through each string in results
            next_results = set()
            for s in results:
                # Loop through each letter in s
                next_results.add("()" + s)
                for j in range(1, len(s) + 1):
                    # Add a string to next_results where we insert () at i
                    new_str = str(s[:j]) + "()" + str(s[j:])
                    next_results.add(new_str)
            
            results = list(next_results)
        
        return sorted(results)
# @lc code=end

