"""
Difficulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/min-stack/description/
Basic Description:
    Create a MinStack class that supports push, pop, top, and getMin methods.
    getMin must be in O(1) time
"""

from typing import List, Union


class MinStack:
    """
    The tricky thing here is to keep a secondary stack for the minimum.
    This will be a monotonic stack, meaning that it will be always decreasing
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Apend the value to the min_stack if it is leq than
        the top of min_stack or if it is empty
        """
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        """
        If the value we just poped is the same as the top of the min_stack
        (meaning it is actually the minimum), we pop it as well from the min_stack
        """
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def run(methods: List[str], args: List[List[int]]) -> List[Union[int, None]]:
    action_dict = {
        "MinStack": MinStack.__init__,
        "push": MinStack.push,
        "pop": MinStack.pop,
        "top": MinStack.top,
        "getMin": MinStack.getMin,
    }
    obj = MinStack()
    result = []
    for i in range(len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))
    return result


if __name__ == "__main__":
    methods = [
        "MinStack",
        "push",
        "push",
        "push",
        "push",
        "getMin",
        "pop",
        "getMin",
        "pop",
        "getMin",
        "pop",
        "getMin",
    ]
    args = [[], [2], [0], [3], [0], [], [], [], [], [], [], []]
    print(run(methods, args))
