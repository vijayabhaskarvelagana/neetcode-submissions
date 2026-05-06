class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        # print(self)
        # print(type(self))
        self.st.append(val)

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]
        return -1

    def getMin(self) -> int:
        if not self.st:
            return -1
        mn = self.st[0]
        for num in self.st:
            mn = min(mn, num)
        return mn


# a = MinStack()
# print(a)
# print(type(a))