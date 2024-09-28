"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Basic Description:
    Create a trie that can search with wildcards .
"""

from typing import List, Union, Dict


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children: Dict[str, Union["TrieNode", None]] = dict()

    def __repr__(self) -> str:
        return f"node:{self.char}"


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)

            root = root.children[char]

        root.children["*"] = None

    def search(self, word: str) -> bool:

        def dfs(root: TrieNode, index: int) -> bool:
            if index == len(word):
                return "*" in root.children

            char = word[index]
            if char != ".":
                if char not in root.children:
                    return False

                return dfs(root.children[char], index + 1)

            for known_char in root.children:
                if known_char != "*" and dfs(root.children[known_char], index + 1):
                    return True

            return False

        return dfs(self.root, 0)


def run(methods: List[str], args: List[List[str]]) -> List[Union[bool, None]]:
    action_dict = {
        "Trie": WordDictionary.__init__,
        "addWord": WordDictionary.addWord,
        "search": WordDictionary.search,
    }
    obj = WordDictionary()
    result = [None]
    for i in range(1, len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))

    return result


if __name__ == "__main__":
    methods = [
        "WordDictionary",
        "addWord",
        "addWord",
        "addWord",
        "search",
        "search",
        "search",
        "search",
    ]
    args = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    print(run(methods, args))
