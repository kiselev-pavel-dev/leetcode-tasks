class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        new_str = ''
        for i in range(len(s)):
            if s[i] not in mapping.keys() and t[i] not in mapping.values():
                mapping[s[i]] = t[i]
            if s[i] in mapping.keys():
                new_str += mapping[s[i]]
            else:
                return False

        return new_str == t
