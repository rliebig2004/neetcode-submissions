class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[r] > nums[0]:
            return nums[0]

        while l <= r:
            k = (l + r) // 2

            if nums[k] > nums[k + 1]:
                return nums[k + 1]
            
            if nums[k] < nums[k - 1]:
                return nums[k]
            
            if nums[k] > nums[0]:
                l = k + 1
            else:
                r = k - 1


        