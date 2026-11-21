class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "[": "]",
            "(": ")",
            "{": "}",
        }
        openBracket = []

        for n in s:
            if n in pair:
                openBracket.append(n)
            elif openBracket:
                if pair[openBracket.pop()] != n:
                    return False
            else:
                return False
        
        if openBracket:
            return False

        return True

        