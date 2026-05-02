class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        target = 0
        n = len(sorted_nums)
        for i in range(n):
            j = i+1
            k = n-1
            while j<k:
                first = sorted_nums[i]
                second = sorted_nums[j]
                third = sorted_nums[k]
                total = first + second + third
                if total == target:
                    if [first, second, third] not in res:
                        res.append([first, second, third])
                    j += 1
                    k -= 1
                elif total > target:
                    k -= 1
                else:
                    j += 1
        return res

        # TC -> O(nlogn) + O(n*n/2) -> O(n**2)
        # SC -> O(n) + O(res*k) where k is average number of elements in earch list item of res -> O(n)