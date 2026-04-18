class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            curr_num = nums[i]
            if target-curr_num in my_dict:
                return [my_dict[target-curr_num], i]
            my_dict[curr_num] = i
        return [] #  edge case