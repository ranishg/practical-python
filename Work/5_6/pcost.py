# pcost.py
#
# Exercise 4.4: Refactor the pcost.py script to use the Stock class.
import report
import sys


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([s.cost for s in portfolio])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Work/Data/portfolio.csv"
    total_cost = portfolio_cost(filename)
    print("Total cost: ", total_cost)
