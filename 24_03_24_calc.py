import operator


class Line:
    n1: float
    n2: float
    op: str
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
    }

    def __init__(self, line: str):
        args = line.split()
        self.n1 = float(args[0])
        self.op = args[1]
        self.n2 = float(args[2])
        if self.op not in self.ops:
            raise f"Unknown operation: {self.op}"

    def __str__(self):
        return f"({self.op} {self.n1} {self.n2})"

    def eval(self) -> int | float:
        return self.ops[self.op](self.n1, self.n2)


if __name__ == "__main__":
    line: str = input("<n1> <op> <n2>: ")
    l: Line = Line(line)
    print(f"{l}\n= {l.eval()}")
