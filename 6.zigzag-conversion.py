#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# "PAYPALISHIRING"\n4

# @lc code=start
class Solution:
    def get_algorithm(self, num_strings: int) -> int:
        """Gets a list of indeces to append strings to"""
        # [0, 3, 2, 5] means first char on 0th string, second on third, third on second, and so on
        
        # Count up to num_strings then back down to 1
        count_up = list(range(num_strings))
        count_down = count_up[1:-1]
        count_down.reverse()
        count_up.extend(count_down)
        return count_up
        # when num_strings is 4:
        # [0, 1, 2, 3]
        # [1, 2]
        
        # when num_strings is 3:
        # [0, 1, 2, 1] repeating
    
    def convert(self, s: str, numRows: int) -> str:
        # Create a list "result" of empty strings of the appropriate length
        strings = [""] * numRows
        algorithm = self.get_algorithm(numRows)
        i_algorithm = 0
        for char in s:
            # Get the index of the next string to add to
            i_next = algorithm[i_algorithm]
            strings[i_next] += char
            
            # Update i_algorithm
            if i_algorithm == len(algorithm) - 1:
                i_algorithm = 0
                continue
            i_algorithm += 1
            
        # Combine list of strings into a single string and return that
        return "".join(strings)
        
# @lc code=end

