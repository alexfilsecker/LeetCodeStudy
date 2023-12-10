"""medium"""

from typing import List, Dict
from collections import Counter
from types import MappingProxyType


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict: Dict[str, List[str]] = dict()
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
