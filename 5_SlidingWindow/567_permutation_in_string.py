from typing import Optional


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        sorted_s1 = sorted(s1)
        substring: Optional[str] = None
        for r in range(len(s1) - 1, len(s2)):
            l = r - len(s1) + 1

            if substring is None:
                substring = s2[0 : r + 1]
            else:
                substring += s2[r]

            if sorted(substring) == sorted_s1:
                return True

            substring = substring[1:]

        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))
