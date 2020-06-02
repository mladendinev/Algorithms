class Stack(object):
    def __init__(self):
        self.o = []
        self.k = []

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.haha = self.__init__()

    def push(self, x: int) -> None:
        self.haha.o.push(x)
        if not self.min_stack:
            self.min_stack = MinStack()
        else:
            if x <= self.min_stack.top():
                self.min_stack.push(x)

    def pop(self) -> None:
        el = self.data.pop()
        if (el == self.min_stack.top()):
            self.min_stack.pop()

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.min_stack.top()


if __name__ == '__main__':
    obj = MinStack()
    obj2 = Stack()

    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
