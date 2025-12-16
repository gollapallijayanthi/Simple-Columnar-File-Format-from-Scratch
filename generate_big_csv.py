import csv
import random

rows = 10000

with open("big_sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "score", "salary"])

    for i in range(1, rows + 1):
        writer.writerow([
            i,
            f"User{i}",
            round(random.uniform(60, 100), 2),
            random.randint(20000, 100000)
        ])

print("big_sample.csv created with", rows, "rows")
