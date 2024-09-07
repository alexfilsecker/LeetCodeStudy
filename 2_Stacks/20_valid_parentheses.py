"""easy 2"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        par = {"(": ")", "{": "}", "[": "]"}
        for p in s:
            print(p, stack)
            if p in par:
                stack.append(p)
            elif len(stack) == 0:
                return False
            elif p != par[stack[-1]]:
                return False
            else:
                stack.pop()

        return len(stack) == 0


if __name__ == "__main__":
    s = "]"
    print(Solution().isValid(s))
