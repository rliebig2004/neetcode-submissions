class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        letters = defaultdict(int)

        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        
        print(letters)

        for n in t:
            if letters[n] == 0:
                return False
            else:
                letters[n] -= 1

        print(letters)
        return True

        