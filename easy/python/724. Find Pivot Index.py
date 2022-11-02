class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left, sum_right = 0, sum(nums[1:])
        nums.append(0)
        for i in range(len(nums) - 1):
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
            sum_right -= nums[i + 1]
        return -1
