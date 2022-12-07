class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        left, right, medium = 0, len(nums), len(nums)//2
        while left <= right:
            if nums[medium] == target:
                idx_min, idx_max = medium, medium
                if len(nums) == 1:
                    return [idx_min, idx_max]
                while idx_min > 0 and nums[idx_min-1] == target:
                    idx_min -= 1
                while idx_max < len(nums)-1 and nums[idx_max+1] == target:
                    idx_max += 1
                return [idx_min, idx_max]
            elif nums[medium] > target:
                left, right, medium = left, medium-1, (left+right)//2
            else:
                left, right, medium = medium+1, right, (left+right)//2
