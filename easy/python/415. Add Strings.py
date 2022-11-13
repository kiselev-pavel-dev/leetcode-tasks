class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n_1, n_2 = 0, 0
        for ch in num1:
            n_1 = n_1*10 + int(ch)
        for ch in num2:
            n_2 = n_2*10 + int(ch)
        result = n_1 + n_2
        if result == 0:
            return '0'
        result_str = ''
        while result > 0:
            result_str = str(result%10) + result_str
            result//=10
        return result_str
