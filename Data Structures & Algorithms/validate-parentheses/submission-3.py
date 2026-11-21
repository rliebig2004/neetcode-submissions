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
            elif not openBracket:
                return False
            else:
                if pair.get(openBracket.pop()) != n:
                    return False
        
        if openBracket:
            return False
            
        return True

        