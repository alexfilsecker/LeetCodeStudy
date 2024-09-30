from typing import Dict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter: Dict[str, int] = dict()
        left, right = 0, 0
        result = 0
        left_moved = False
        while right < len(s):
            # print()
            # print("window:", s[left : right + 1])
            right_char = s[right]
            if not left_moved:
                if right_char not in counter:
                    counter[right_char] = 1
                else:
                    counter[right_char] += 1
            else:
                left_moved = False
            print(counter)

            most_common = max(counter.values())
            window_size = right - left + 1
            # print("most_common:", most_common, "window_size:", window_size)

            # Check if window is valid
            if window_size - most_common <= k:
                # print("valid")
                result = max(result, window_size)
                # print("result: ", result)
                right += 1
            else:
                # print("not valid")
                counter[s[left]] -= 1
                left += 1
                left_moved = True
                if left == len(s) - 1:
                    break

        return result


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s, k))
