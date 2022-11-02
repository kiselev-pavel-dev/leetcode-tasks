class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dict_number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        temp = 0
        for i in range(len(s) - 1):
            if dict_number[s[i + 1]] > dict_number[s[i]]:
                temp = dict_number[s[i]]
            else:
                result += dict_number[s[i]] - temp
                temp = 0
        result += dict_number[s[-1]] - temp
        return result
