class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, i, j, l1, l2, front_prod, back_prod = len(nums), 0, len(nums)-1, [], [], 1, 1
        while i<n:
            l1.append(front_prod)
            front_prod *= nums[i]
            i += 1
        print(f"l1: {l1}")
        while j>=0:
            l2.append(back_prod)
            back_prod *= nums[j]
            j -= 1
        print(f"l2: {l2}")
        reversed_l2 = l2[::-1]
        result = []
        k = 0
        while k<n:
            temp_res = (l1[k] * reversed_l2[k])
            result.append(temp_res)
            k += 1
        return result