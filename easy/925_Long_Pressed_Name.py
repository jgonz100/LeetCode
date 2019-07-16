"""Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
"""

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        stack = []
        for c in name:
            stack.insert(0, c)
        for c in typed:
            try:
                if c == stack[len(stack)-1]:
                    stack.pop()
                if stack == []:
                    break
            except:
                pass
        if stack == []:
            return True
        else:
            return False