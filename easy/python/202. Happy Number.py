class Solution:
    def isHappy(self, n: int) -> bool:
        result = []
        while n > 0:
            temp, res = n, 0
            while temp > 0:
                res += (temp % 10) ** 2
                temp //= 10
            if res == 1:
                return True
            if res in result:
                return False
            result.append(res)
            n = res
