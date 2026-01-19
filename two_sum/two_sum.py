class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_map = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in my_map:
                return [my_map[diff], i]
            my_map[num] = i
        return []
        
