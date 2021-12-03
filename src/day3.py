from collections import Counter
from pathlib import Path

def read_input(path):
    lines = path.read_text().splitlines()
    # Paranoia - make sure all lines are the same length
    maxlen = max(len(l) for l in lines)
    lines = [l.rjust(maxlen, "0") for l in lines]
    return lines

def count_bits(lines, pos):
    c = Counter(l[pos] for l in lines)
    mc = c.most_common()
    most, most_count = mc[0]
    least, least_count = mc[-1]

    # Special case if there are the same number
    if most_count == least_count:
        return "1", "0"
    return most, least

def power(lines):
    gamma = ""
    epsilon = ""
    for pos in range(len(lines[0])):
        most, least = count_bits(lines, pos)
        gamma += most
        epsilon += least
    return gamma, epsilon

def search(lines, least=False):
    for i in range(len(lines[0])):
        # Hack here - index by least which is a bool
        lines = [l for l in lines if l[i] == count_bits(lines, i)[least]]
        if len(lines) == 1:
            return lines[0]
    assert len(lines) > 1, "Too many lines left"
    assert True, "How can this happen?"


if __name__ == "__main__":
    path = Path("inputs/day3.txt")
    lines = read_input(path)
    gamma, epsilon = power(lines)
    power = int(gamma,2) * int(epsilon,2)
    print(f"Power consumption is {power} ({gamma=}, {epsilon=})")

    oxygen = search(lines, least=False)
    co2 = search(lines, least=True)
    life_support = int(oxygen, 2) * int(co2, 2)
    print(f"Life support is {life_support} ({oxygen=}, {co2=})")
