"""
Difficulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/valid-sudoku/description/
Basic Description: 
    See if a board is a valid sudoku
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        What we do is to create sets, one for each row, column and box.
        """
        # Create all column sets
        col_sets = [set() for _ in range(9)]

        # Traverse the sudoku rows
        for row_index, row in enumerate(board):
            # Create the row set for this row
            row_set = set()

            # Create the box sets every 3 rows
            if row_index % 3 == 0:
                box_sets = [set() for _ in range(3)]

            # Traverse the sudoku values
            for col_index, value in enumerate(row):
                if value != ".":

                    # Check the row set
                    if value in row_set:
                        return False
                    row_set.add(value)

                    # Check the box set
                    if value in box_sets[col_index // 3]:
                        return False
                    box_sets[col_index // 3].add(value)

                    # Check the col set
                    if value in col_sets[col_index]:
                        return False
                    col_sets[col_index].add(value)

        return True


if __name__ == "__main__":
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(Solution().isValidSudoku(board))
