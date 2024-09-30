"""
dificulty: hard
times completed: 1
link: https://leetcode.com/problems/sliding-window-maximum/description/
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        To solve this problem we use a deque. Basically we keep trak of an always decreasing
        queue of the maximum values. When r reaches a new value, we place it in the queue ensuring
        that we remain with the higher values. When l reaches that value, we pop it because it is no longer
        in the window.
        """

        # The queue will store the positions of the values, not the values.
        queue = deque()

        r, l = 0, 0
        output = []
        while r < len(nums):
            # First, pop all values from the queue that are lower than the new value
            # that has been seen by r
            while len(queue) > 0 and nums[queue[-1]] < nums[r]:
                queue.pop()

            # Append the new value, wich will be always lower than the top of the queue
            # since we did the previous while
            queue.append(r)

            # Remove the element if the left pointer has surpassed it since we need
            # to maintain the window size
            if l > queue[0]:
                queue.popleft()

            # Check that our window has reached the desired width k
            if r + 1 >= k:
                # The left most value is the maximum value of the window
                output.append(nums[queue[0]])

                l += 1  # Only increase l when we have reached the desired width

            r += 1

        return output


if __name__ == "__main__":
    nums = [7, 6, 5, 4, 3, 2, 1, 0]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
