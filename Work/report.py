# report.py
#
# Exercise 2.4

import csv
import sys


def read_portfolio(filename):
    portfolio = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {}
            holding["name"] = row[0]
            holding["shares"] = int(row[1])
            holding["price"] = float(row[2])
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, "r") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def main(argv):
    if len(argv) == 3:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
    else:
        portfolio_filename = "Work/Data/portfolio.csv"
        prices_filename = "Work/Data/prices.csv"

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    total_cost = 0.0
    for holding in portfolio:
        total_cost += holding["shares"] * holding["price"]
    print("Total cost: ", total_cost)

    current_value = 0.0
    for holding in portfolio:
        current_value += holding["shares"] * prices[holding["name"]]
    print("Current value: ", current_value)

    gain_loss = current_value - total_cost
    print("Gain/Loss: ", gain_loss)


if __name__ == "__main__":
    main(sys.argv)
