class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s, reverse=True))
        t_sorted = "".join(sorted(t, reverse=True))
        return s_sorted == t_sorted