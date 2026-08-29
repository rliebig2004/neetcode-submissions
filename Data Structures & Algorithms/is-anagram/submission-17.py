class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = defaultdict(int)

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        print(seen)
        
        for n in t:
            if seen[n] <= 0 or n not in seen:
                return False
            else:
                seen[n] -= 1

        print(seen)
        return True