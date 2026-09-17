class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d1 = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in d1:
                return [d1[diff], i]
            d1[n] = i
        
        return []