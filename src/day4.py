from pathlib import Path

class Board:
    def __init__(self, rows):
        # 5x5 array or map num->row,col,seen?
        self.numbers = {}
        for i, row in enumerate(rows):
            for j, num in enumerate(row):
                self.numbers[num] = (i, j, False)
    def has_won(self):
        rows = [0,0,0,0,0]
        cols = [0,0,0,0,0]
        for i, j, seen in self.numbers.values():
            if not seen:
                continue
            rows[i] += 1
            cols[j] += 1
        return any(n==5 for n in rows) or any(n==5 for n in cols)
    def see(self, num):
        if num not in self.numbers:
            return
        i, j, _ = self.numbers[num]
        self.numbers[num] = (i, j, True)
    def score(self):
        return sum(n for n in self.numbers if not self.numbers[n][2])

def read_input(path):
    lines = path.read_text().splitlines()
    randoms = [int(n) for n in lines[0].split(",")]

    boards = []

    top = 2
    while top < len(lines):
        boards.append(Board([
            [int(n) for n in row.split()]
            for row in lines[top:top+5]
        ]))

        top += 6

    return randoms, boards

def run_puzzle(randoms, boards):
    winners = set()
    for n in randoms:
        for i, b in enumerate(boards):
            if i in winners:
                continue
            b.see(n)
            if b.has_won():
                score = b.score()
                winners.add(i)
                if len(winners) == 1:
                    print(f"Board {i+1} won first with {n}, score {score}")
                    print(f"Result = {n*score}")
                elif len(winners) == len(boards):
                    print(f"Board {i+1} has finally won with {n}, score {score}")
                    print(f"Result = {n*score}")
                    return

if __name__ == "__main__":
    path = Path("samples/day4.txt")
    randoms, boards = read_input(path)

    assert randoms[:4] == [7,4,9,5]
    for b in boards:
        print("-" * 20)
        print(len(b.numbers))
        print(b.numbers)
    assert len(boards) == 3, f"Got {len(boards)} boards"
    assert boards[0].numbers[22] == (0,0,False)
    run_puzzle(randoms, boards)

    path = Path("inputs/day4.txt")
    randoms, boards = read_input(path)
    run_puzzle(randoms, boards)
