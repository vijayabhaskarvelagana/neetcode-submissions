class Solution:
    def hammingWeight(self, n: int) -> int:
        n_copy = n
        count = 0
        while(n_copy):
            if n_copy&1:
                count += 1
            n_copy >>= 1
        return count