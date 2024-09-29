"""
Dificulty: Easy
Times Completed: 1
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Basic Description:
    Create a class that keeps track of the kth largest element
"""

from typing import List, Union

import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def run(methods: List[str], args: List[List[str]]) -> List[Union[int, None]]:
    action_dict = {"KthLargest": KthLargest.__init__, "add": KthLargest.add}
    obj = KthLargest(*args[0])
    result = [None]
    for i in range(1, len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))

    return result


if __name__ == "__main__":
    methods = ["KthLargest", "add", "add", "add", "add", "add"]
    args = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    print(run(methods, args))
