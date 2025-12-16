import sys, csv
from reader import read_custom

inp, out = sys.argv[1], sys.argv[2]
cols = sys.argv[3:] if len(sys.argv) > 3 else None

data = read_custom(inp, cols)

with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(data.keys())
    for i in range(len(next(iter(data.values())))):
        w.writerow([data[c][i] for c in data])
