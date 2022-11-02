class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            current_str = ''
            if i % 3 == 0:
                current_str += 'Fizz'
            if i % 5 == 0:
                current_str += 'Buzz'
            if current_str == '':
                result.append(str(i))
            else:
                result.append(current_str)
        return result
