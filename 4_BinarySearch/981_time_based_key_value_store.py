"""medium"""

from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.dic: Dict[str, List[Tuple[str, int]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((value, timestamp))
        print("set returned none")

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.dic:
            return res

        values = self.dic[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_timestamp = values[mid][1]
            if mid_timestamp <= timestamp:
                res = values[mid][0]
                left = mid + 1

            else:
                right = mid - 1

        print("get", key, timestamp, "returned", res)
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == "__main__":
    functions = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    parameters = [
        [],
        ["foo", "bar", 1],
        ["foo", 1],
        ["foo", 3],
        ["foo", "bar2", 4],
        ["foo", 4],
        ["foo", 5],
    ]
    obj = None
    for i in range(len(functions)):
        if functions[i] == "TimeMap":
            obj = TimeMap()
        elif functions[i] == "set":
            obj.set(*parameters[i])
        elif functions[i] == "get":
            obj.get(*parameters[i])
