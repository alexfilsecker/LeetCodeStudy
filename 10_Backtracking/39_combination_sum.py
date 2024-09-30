"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/combination-sum/description/
Basic Description:
    Given a candidate list, return all the combinations of them that add up to target
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        What we have to do is a dfs of a descision tree.
        On every candidate, we have the option of either continue using it
        or never use it again. So we keep an index that says over which
        candidate we are working
        """

        res = []

        def dfs(index: int, current: List[int], total: int) -> None:
            # Good base case
            if total == target:
                res.append(current.copy())
                return

            # Bad base cases
            if index >= len(candidates) or total > target:
                return

            # Path where we continue to use the indexed candidate
            current.append(candidates[index])
            dfs(index, current, total + candidates[index])

            # Neve use that candidate again
            current.pop()
            dfs(index + 1, current, total)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
