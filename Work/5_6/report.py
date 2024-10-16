# report.py
#
# Exercise 4.4: Refactor the report.py script to use the Stock class.

import fileparse
from stock import Stock
import tableformat
import sys


def read_portfolio(filename):
    portfolio = []
    with open(filename) as lines:
        records = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )

    portfolio = [
        Stock(record["name"], record["shares"], record["price"]) for record in records
    ]
    return portfolio


def read_prices(filename):
    with open(filename) as lines:
        prices = fileparse.parse_csv(lines, types=[str, float], has_headers=False)
        prices = dict(prices)
    return prices


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        current_price = prices[holding.name]
        change = current_price - holding.price
        summary = (holding.name, holding.shares, current_price, change)
        report.append(summary)
    return report


def print_report(reportdata, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) == 3:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
    else:
        portfolio_filename = "Work/Data/portfolio.csv"
        prices_filename = "Work/Data/prices.csv"

    portfolio_report(portfolio_filename, prices_filename, "txt")


if __name__ == "__main__":
    main(sys.argv)
