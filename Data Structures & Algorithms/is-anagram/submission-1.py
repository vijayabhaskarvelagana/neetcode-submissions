class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s, reverse=True))
        t_sorted = "".join(sorted(t, reverse=True))
        print(s_sorted)
        print(t_sorted)
        print(s[::-1])
        print(s)
        return s_sorted == t_sorted