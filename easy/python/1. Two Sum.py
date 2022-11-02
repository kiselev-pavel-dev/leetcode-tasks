class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind, number in enumerate(nums):
            if target - number in nums[ind + 1 :]:
                result_index_left = ind
                find = target - number
        for ind, number in enumerate(nums):
            if number == find and ind != result_index_left:
                return [result_index_left, ind]
