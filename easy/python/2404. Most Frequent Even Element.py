class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        for item in nums:
            if item % 2 == 0:
                if item in dic.keys():
                    dic[item] += 1
                else:
                    dic[item] = 1
        if len(dic) == 0:
            return -1
        max_count, max_key = 0, 0
        for key, value in dic.items():
            if value > max_count:
                max_count = value
                max_key = key
            if value == max_count:
                if key < max_key:
                    max_key = key
        return max_key
