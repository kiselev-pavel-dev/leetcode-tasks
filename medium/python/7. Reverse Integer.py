class Solution:
    def reverse(self, x: int) -> int:
        new_x = 0
        minus = False
        if x < 0:
            minus = True
            x *= -1
        while x > 0:
            new_x = new_x * 10 + (x % 10)
            x //= 10
        if new_x > pow(2, 31):
            return 0
        if minus:
            return -1 * new_x
        return new_x
