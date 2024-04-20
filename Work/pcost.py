# pcost.py
#
# Exercise 1.27

total_cost = 0
with open("Work/Data/portfolio.csv", "r") as f:
    headers = next(f).strip().split(",")
    for line in f:
        row = line.strip().split(",")
        total_cost += int(row[1]) * float(row[2])

    print("Total cost: ", total_cost)
