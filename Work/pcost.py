# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            total_cost += int(row[1]) * float(row[2])
    return total_cost


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Work/Data/portfolio.csv"
    total_cost = portfolio_cost(filename)
    print("Total cost: ", total_cost)
