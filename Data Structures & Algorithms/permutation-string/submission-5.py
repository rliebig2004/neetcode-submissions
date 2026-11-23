class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        check = defaultdict(int)
        count = defaultdict(int)
        l = 0
        
        for n in s1:
            check[n] += 1

        for r, s in enumerate(s2):
            count[s] += 1
            if (r - l + 1) > window:
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
            
            if (r - l + 1) == window and count == check:
                return True

        print(check, count)
        return False

        