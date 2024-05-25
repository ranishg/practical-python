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
        for row_no, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {row_no}: Couldn't convert: {row}")
    return total_cost


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Work/Data/portfolio.csv"
    total_cost = portfolio_cost(filename)
    print("Total cost: ", total_cost)
