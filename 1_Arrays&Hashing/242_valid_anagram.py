"""easy"""

from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def hash_str(string: str) -> Dict[str, int]:
            char_hash: Dict[str, int] = {}
            for char in string:
                if char in char_hash:
                    char_hash[char] += 1
                else:
                    char_hash[char] = 1

            return char_hash

        s_char_hash = hash_str(s)
        t_char_hash = hash_str(t)

        letters = set(s_char_hash.keys()).union(set(t_char_hash.keys()))

        for letter in letters:
            try:
                if s_char_hash[letter] != t_char_hash[letter]:
                    return False
            except KeyError:
                return False

        return True


if __name__ == "__main__":
    s = "anagran"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
