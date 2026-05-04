class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            # print(ch)
            if st and st[-1]+ch in ['()', '{}', '[]']:
                print(st[-1]+ch)
                st.pop()
            else:
                st.append(ch)

        return len(st) == 0
