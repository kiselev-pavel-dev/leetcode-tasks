class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_nums = {}
        for item in nums:
            if item not in count_nums.keys():
                count_nums[item] = 1
            else:
                count_nums[item] += 1
        for key, val in count_nums.items():
            if val == 1:
                return key
