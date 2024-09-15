"""
Difficulty: Easy
Times Completed: 2
Link: https://leetcode.com/problems/valid-parentheses/description/
Basic Description:
    Check if a string of parenthesis is valid or not
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        We use a stack to keep track of the openings and closings.
        We append all openings and remove the openings when we see
        the apropiate closing.
        """

        # Crate the stack as a list
        # You'll see that it only contains the openings
        stack: List[str] = []

        # Create a dictionary for two reasons.
        # 1. To know what are the posible openings
        # 2. To know what is the corresponding closing for each opening
        pars = {"(": ")", "{": "}", "[": "]"}

        # We traverse the string
        for p in s:

            # Check if the character is an opening
            if p in pars:
                stack.append(p)

            # There are no openings to close in the stack
            elif len(stack) == 0:
                return False
            # The closing we are seing does not match the last opening in the stack
            elif p != pars[stack[-1]]:
                return False

            # It was a match so we pop the top of the stack
            else:
                stack.pop()

        # There should not be any remaining openings in the stack
        return len(stack) == 0


if __name__ == "__main__":
    s = "]"
    print(Solution().isValid(s))
