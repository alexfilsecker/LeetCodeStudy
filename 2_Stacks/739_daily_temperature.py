from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = []
        result: List[int] = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((i, t))
            else:
                while len(stack) > 0 and t > stack[-1][1]:
                    index, _ = stack.pop()
                    result[index] = i - index

                stack.append((i, t))

        return result


if __name__ == "__main__":
    temperatures = [30, 40, 50, 60]
    print(Solution().dailyTemperatures(temperatures))
