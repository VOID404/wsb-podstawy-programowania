import enum


class Operation(enum.StrEnum):
    Add = "+"
    Sub = "-"
    Mul = "*"
    Div = "/"

    def eval(self, n1: int | float, n2: int | float) -> int | float:
        match self:
            case Operation.Add: return n1 + n2
            case Operation.Sub: return n1 - n2
            case Operation.Mul: return n1 * n2
            case Operation.Div: return n1 / n2


class Line:
    n1: float
    n2: float
    op: Operation

    def __init__(self, line: str):
        args = line.split()
        self.n1 = float(args[0])
        self.op = Operation(args[1])
        self.n2 = float(args[2])

    def __str__(self):
        return f"({self.op} {self.n1} {self.n2})"

    def eval(self) -> int | float:
        return self.op.eval(self.n1, self.n2)


if __name__ == "__main__":
    line: str = input("<n1> <op> <n2>: ")
    l: Line = Line(line)
    print(f"{l}\n= {l.eval()}")
