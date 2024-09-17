"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/lru-cache/description/
Basic Description:
    Implement an LRU cache that supports a get and a put method
    LRU means least recently used. So given a certain capacity for 
    the LRU, when we try to put more than that capacity into the cache
    we need to evict the last recently used element
"""

from typing import List, Optional, Dict


class Node:
    """This is a simple node of a dll"""

    def __init__(
        self,
        key: int,
        val: int,
        left: "Optional[Node]" = None,
        right: "Optional[Node]" = None,
    ):
        self.key = key
        self.val = val
        self.prev = left
        self.next = right


class LRUCache:
    """
    To solve this problem, we first create a hashmap for storing the actual data
    Each value of the hashmap points to a node in a doubly linked list. They are the
    ones that actualy store the values. When we get something from the hashmap,
    we need to update the dll to make the node we got the most recently used. In the
    same way, when we put something it is always going to be placed into the most recently
    used position. If we exceed the capacity of the lru cache, we need to evict the lru
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = dict()

        # Dummy nodes
        self.left = Node(0, 0)  # LRU: Last recently used
        self.right = Node(0, 0)  # Most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        """Has to be inserted to the right"""
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right

    def remove(self, node: Node):
        """Remove from the list"""
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        """
        retrieve the node from the cache, and update it to the most recently used
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        """
        Always place new key-values into the mru, if the capacity is exceeded,
        we need to clean up.
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Check capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def run(methods: List[str], args: List[List[int]]) -> None:
    action_dict = {
        "LRUCache": LRUCache.__init__,
        "put": LRUCache.put,
        "get": LRUCache.get,
    }
    obj = LRUCache(*args[0])
    result = [None]
    for i in range(1, len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))

    return result


if __name__ == "__main__":
    methods = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    result = run(methods, args)
    print(result)
