#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
"""
1. Binary search until with find target
2. Iterate left and right until both left and right are not equal to target
3. return indeces
O(log n * n / 2)

1. Binary search for index directly left of number and directly right of number
O(2log n)
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        1. While lo is less than hi
        2. Calculate mid
        3. If mid value is less than target, 
        """
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                print(f"{lo}, {hi}")
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        print()
        hi = search(target+1)-1
        
        return [lo, hi] if lo <= hi else [-1, -1]
        
# @lc code=end

