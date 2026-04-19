class Solution:
    def countOneBits(self, i: int) -> int:
        copy_i = i
        count = 0
        while copy_i:
            if copy_i & 1:
                count += 1
            copy_i >>= 1
        return count

    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            print(f"self: {self}")
            print(f"self.countOneBits: {self.countOneBits}")
            result_i = Solution.countOneBits(self, i) # this can also be written self.CountOneBits(i)
            result.append(result_i)
        return result