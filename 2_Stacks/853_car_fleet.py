from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(position[i], speed[i]) for i in range(len(position))]
        ps = sorted(ps, key=lambda x: x[0], reverse=True)
        leader = 0
        n = 0
        for p, s in ps:
            t = (target - p) / s
            if t > leader:
                leader = t
                n += 1

        return n


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(Solution().carFleet(target, position, speed))
