"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/
Basic Description:
    Create a Trie, that can perform insert, search and startsWith
"""

from typing import List, Union, Dict


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children: Dict[str, Union["TrieNode", None]] = dict()


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)

            root = root.children[char]

        root.children["*"] = None

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            if char not in root.children:
                return False

            root = root.children[char]

        return "*" in root.children

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False

            root = root.children[char]

        return True


def run(methods: List[str], args: List[List[str]]) -> List[Union[bool, None]]:
    action_dict = {
        "Trie": Trie.__init__,
        "insert": Trie.insert,
        "search": Trie.search,
        "startsWith": Trie.startsWith,
    }
    obj = Trie()
    result = [None]
    for i in range(1, len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))

    return result


if __name__ == "__main__":
    methods = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    print(run(methods, args))
