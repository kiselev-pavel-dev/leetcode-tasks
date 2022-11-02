class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = ''
        dic = {'[': ']', '(': ')', '{': '}'}
        for ch in s:
            if ch in dic.keys():
                stack += ch
            else:
                if stack == '':
                    return False
                if dic[stack[-1]] != ch:
                    return False
                stack = stack[:-1]
        return stack == ''
