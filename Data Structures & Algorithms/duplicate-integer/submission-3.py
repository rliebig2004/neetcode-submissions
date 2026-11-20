class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        passed = set()

        for i in nums:
            if i in passed:
                return True

            passed.add(i)
        return False