class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dic = {}
        n = len(nums)
        for item in nums:
            if item not in dic.keys():
                dic[item] = 1
            else:
                dic[item] += 1
                if dic[item] > n // 2:
                    return item
