"""medium"""

from typing import List
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []

        def dfs(left: int, right: int, node: str):
            if len(node) == 2 * n:
                result.append(node)
                return
            else:
                pass

            if left < n:
                dfs(left + 1, right, node + "(")

            if right < left:
                dfs(left, right + 1, node + ")")

        dfs(0, 0, "")
        return result


if __name__ == "__main__":
    for n in range(1, 20):
        print(n, len(Solution().generateParenthesis(n)))
