class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # d1 = {}

        # for ch in s:
        #     d1[ch] = d1.get(ch, 0) + 1
        # for ch in t:
        #     d1[ch] = d1.get(ch, 0) - 1
        
        # for k,v in d1.items():
        #     if v != 0:
        #         return False
        
        # return True

        return Counter(s) == Counter(t)

        