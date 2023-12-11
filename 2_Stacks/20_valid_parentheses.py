class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maches = {"(": ")", "{": "}", "[": "]"}
        for parentheses in s:
            if len(stack) == 0:
                if parentheses not in maches:
                    return False
                stack.append(parentheses)
            else:
                last = stack[-1]
                if last in maches:
                    if parentheses not in maches:
                        if parentheses != maches[last]:
                            return False
                        else:
                            stack.pop()

                    else:
                        stack.append(parentheses)

        return len(stack) == 0


if __name__ == "__main__":
    s = "({[]}()])"
    print(Solution().isValid(s))
