"""
dificulty: hard
completed times: 1
link: https://leetcode.com/problems/minimum-window-substring/description/
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        l = 0
        t_count = Counter(t)
        # Do a sliding window algorithm
        s_count = Counter()
        for r in range(len(s)):
            r_char = s[r]
            if r_char in s_count:
                s_count[r_char] += 1
            else:
                s_count[r_char] = 1

            # Check if it is a valid substring
            valid = True

            while valid:
                # print()
                # Create the substring
                substring = s[l : r + 1]

                for char, char_count in t_count.items():
                    if char not in s_count or char_count > s_count[char]:
                        valid = False
                        break

                # print(substring, valid)
                # If valid, we shrink the window}
                if valid:
                    if result == "" or len(substring) < len(result):
                        result = substring
                    if l < r:
                        l_char = s[l]
                        s_count[l_char] -= 1
                        l += 1
                    else:
                        valid = False

        return result


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
