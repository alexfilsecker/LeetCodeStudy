"""easy 2"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        refactored = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        for i in range(len(refactored) // 2):
            if refactored[i] != refactored[-(i + 1)]:
                return False

        return True


if __name__ == "__main__":
    s = "raceacar"
    print(Solution().isPalindrome(s))
