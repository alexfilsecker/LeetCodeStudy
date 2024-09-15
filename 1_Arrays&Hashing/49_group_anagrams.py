"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/group-anagrams/description/
Basic Description: 
    You are given an array of strings, group the ones that are anagrams
    between each other
"""

from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The solution is quite simple, just sort the strings and compare
        them with a hashmap. Basically if two sorted strings are the same,
        it means they are anagrams.
        """

        # Create the dictionary.
        # The keys are gonna be the sorted strings or the anagrams sorted state
        # And the values are the list of grouped anagrams
        anagram_dict: Dict[str, List[str]] = dict()

        # Traverse the string array
        for string in strs:
            anagram = "".join(sorted(string))
            if anagram in anagram_dict:
                anagram_dict[anagram].append(string)
            else:
                anagram_dict[anagram] = [string]

        return anagram_dict.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
