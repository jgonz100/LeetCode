"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            char_arr = str(x)[::-1]
        else:
            char_arr = '-' + str(x)[:0:-1]
            
        ans = int(char_arr)
        
        if ans > (1<<31) - 1 or ans < (1<<31) * -1:
            return 0
        else:
            return an