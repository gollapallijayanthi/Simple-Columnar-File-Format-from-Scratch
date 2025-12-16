import csv, time
from reader import read_custom

start = time.time()
with open("big_sample.csv") as f:
    r = csv.reader(f)
    next(r)
    _ = [row[2] for row in r]
print("CSV time:", time.time() - start)

start = time.time()
read_custom("big_sample.custom", ["score"])
print("Custom selective read time:", time.time() - start)
