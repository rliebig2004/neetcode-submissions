class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        checked = {}
        
        for i in s:
            if i in checked:
                checked[i] += 1
            else:
                checked[i] = 1
        for n in t: 
            if n not in checked or checked[n] == 0:
                return False
            else:
                checked[n] -= 1
        return True
        