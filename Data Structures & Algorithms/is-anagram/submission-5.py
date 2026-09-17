class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        # if len(s) != len(t):
        #     return False

        # d1 = {}

        # for char in s:
        #     d1[char] = d1.get(char, 0) + 1
        # for char in t:
        #     d1[char] = d1.get(char, 0) - 1

        # for k, v in d1.items():
        #     if v != 0:
        #         return False
        
        # return True

        