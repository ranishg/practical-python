# pcost.py
#
# Exercise 1.27
import fileparse
import sys


def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as lines:
        records = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )

        for record in records:
            total_cost += record["shares"] * record["price"]

    return total_cost


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Work/Data/portfolio.csv"
    total_cost = portfolio_cost(filename)
    print("Total cost: ", total_cost)
