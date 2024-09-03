"""easy 2"""

from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # hash s
        hash: Dict[str, int] = {}
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        # Iterate over t
        print(hash)
        for char in t:
            if char not in hash:
                print("char", char, "not in hash")
                return False
            if hash[char] == 0:
                return False

            hash[char] -= 1

        return True


if __name__ == "__main__":
    s = "anagran"
    t = "nagaran"
    print(Solution().isAnagram(s, t))
