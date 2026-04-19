class Solution:
    def reverseBits(self, n: int) -> int:
        n_copy = n
        total_bits = 32
        res = 0
        while total_bits:
            if n_copy & 1:
                res += pow(2, total_bits-1)
            n_copy >>= 1
            total_bits -= 1
        return res
