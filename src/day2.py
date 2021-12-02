from pathlib import Path
from dataclasses import dataclass

def read_input(path):
    instructions = []
    for line in path.open():
        verb, amount = line.strip().split()
        amount = int(amount)
        instructions.append((verb, amount))
    return instructions

@dataclass
class Pos:
    distance: int = 0
    depth: int = 0
    aim: int = 0

    def apply(self, instruction):
        verb, n = instruction
        match verb:
            case "forward": self.distance += n
            case "up": self.depth -= n
            case "down": self.depth += n

    def better_apply(self, instruction):
        verb, n = instruction
        match verb:
            case "forward":
                self.distance += n
                self.depth += n * self.aim
            case "up": self.aim -= n
            case "down": self.aim += n

if __name__ == "__main__":
    infile = Path("inputs/day2.txt")
    instructions = read_input(infile)
    print(f"We have {len(instructions)} instructions")
    print(f"Verbs are {set(v for v,n in instructions)}")
    p = Pos()
    for i in instructions:
        p.apply(i)
    print(p)
    print(f"Solution is: {p.distance * p.depth}")
    p = Pos()
    for i in instructions:
        p.better_apply(i)
    print(p)
    print(f"Solution is: {p.distance * p.depth}")
