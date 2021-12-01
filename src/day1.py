import collections
from itertools import islice

with open("inputs/day1_1.txt") as f:
    inputs = [int(l.strip()) for l in f]

print(sum(x > y for x, y in zip(inputs[1:], inputs[:-1])))

# Answer: 1266

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

totals = [sum(g) for g in sliding_window(inputs, 3)]
print(sum(x > y for x, y in zip(totals[1:], totals[:-1])))

# Answer: 1217

