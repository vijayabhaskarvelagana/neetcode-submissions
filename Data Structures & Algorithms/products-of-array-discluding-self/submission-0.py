class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        result = []
        while i<n:
            prod = 1
            j = 0
            while j<n:
                if j == i:
                    j += 1
                    continue
                prod *= nums[j]
                j += 1
            result.append(prod)
            i += 1
        return result