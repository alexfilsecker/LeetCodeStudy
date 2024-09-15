"""
Difficulty: Easy
Times Completed: 2
Link: https://leetcode.com/problems/valid-anagram/description/
Basic Description:
    Check if two strings have the same letters the same
    amount of times
"""

from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        What we do is to create a counter of the characters in the first
        string, and then traverse the second string comparing it with the
        previous hash
        """

        # If both strings are not of the same lenght the answer is trivial
        if len(s) != len(t):
            return False

        # Create a counter of s
        # Could also been done with counter(s) from the "collections" library
        hash: Dict[str, int] = {}
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        # Traverse the second string
        for char in t:
            # A char in t doesen't appear in s
            if char not in hash:
                print("char", char, "not in hash")
                return False
            # A char in t appears more times in t than in s
            if hash[char] == 0:
                return False

            # Decrease the number of that char left to compare
            # in the hash
            hash[char] -= 1

        return True


if __name__ == "__main__":
    s = "anagran"
    t = "nagaran"
    print(Solution().isAnagram(s, t))
