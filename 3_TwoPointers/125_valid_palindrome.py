"""easy"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        refactored = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        last = len(refactored) - 1
        for i in range(0, len(refactored) // 2):
            if refactored[i] != refactored[last - i]:
                return False

        return True


if __name__ == "__main__":
    s = "race a car"
    print(Solution().isPalindrome(s))
