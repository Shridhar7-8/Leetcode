class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res=[]
        my_map = {}
        for i in range(len(nums)):
            my_map[i] = nums[i]
            diff = target - nums[i]
            if diff in my_map.values():
                j = nums.index(diff)
                if i!=j:
                    res.extend((i,j))
        return res
