class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_customer = 0
        for item in accounts:
            if sum(item) > max_customer:
                max_customer = sum(item)
        return max_customer
