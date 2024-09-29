"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/task-scheduler/description/
Basic Description:
    We have tasks, A-Z and a "resting time" n. The same task cannot
    be done until n cycles so you gotta let them cook. Return the
    minimum intervals required to complete all tasks
"""

from typing import List, Tuple, Optional
from collections import Counter, deque
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        # Create a priority queue
        heap: List[Tuple[int, str]] = [
            (-1 * count, task) for task, count in counter.items()
        ]
        heapify(heap)
        # print(heap)

        interval_counter = 0
        queue = deque()
        while heap or queue:
            if heap:
                count, task = heappop(heap)
                if count < -1:
                    queue.append((count + 1, task, interval_counter + n + 1))

            interval_counter += 1

            while queue and queue[0][2] == interval_counter:
                count, task, _ = queue.popleft()
                heappush(heap, (count, task))

        return interval_counter


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))
