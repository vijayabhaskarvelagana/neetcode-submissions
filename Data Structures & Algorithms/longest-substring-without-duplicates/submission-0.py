class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(0, n):
            curr_set = set()
            for j in range(i, n):
                if s[j] not in curr_set:
                    curr_set.add(s[j])
                else:
                    break
            max_len = max(max_len, len(curr_set))
        return max_len

        # TC -> O(n*n) -> O(n**2)
        # SC -> O(n)
                

