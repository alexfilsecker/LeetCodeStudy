"""medium"""

from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_map: Dict[str, int] = dict()
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char not in char_map or char_map[char] < left:
                char_map[char] = right
                max_length = max(max_length, right - left + 1)
            else:
                left = char_map[char] + 1
                char_map[char] = right

        return max_length


if __name__ == "__main__":
    s = "tmmzuxt"
    print(Solution().lengthOfLongestSubstring(s))
