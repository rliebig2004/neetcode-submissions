class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            k = (l + r) // 2

            if nums[k] == target:
                return k
            
            # window is either entirely left/right side
            if nums[l] <= nums[k]:
                if target > nums[k] or target < nums[l]:
                    l = k + 1
                else:
                    r = k - 1
            
            # k is after the invert point
            else:
                if target < nums[k] or target > nums[r]:
                    r = k - 1
                else:
                    l = k + 1
            
        return -1
                    

