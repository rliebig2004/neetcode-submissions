class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        stack = []

        for n in s:
            if n in pair:
                if stack and stack.pop() == pair[n]:
                    continue
                else:
                    return False
            else:
                stack.append(n)

        return True if not stack else False

        