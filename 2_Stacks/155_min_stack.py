"""medium"""

from typing import List, Union


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
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
