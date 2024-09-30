"""medium"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a: int, b: int) -> int:
            return a + b

        def substract(a: int, b: int) -> int:
            return a - b

        def multiply(a: int, b: int) -> int:
            return a * b

        def divide(a: int, b: int) -> int:
            return int(a / b)

        operands = {"+": add, "-": substract, "*": multiply, "/": divide}
        stack = []
        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                result = operands[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    tokens = ["4", "13", "5", "/", "+"]
    print(Solution().evalRPN(tokens))
