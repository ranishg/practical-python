# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    filename,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    with open(filename, "r") as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers if there are any
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:
                continue
            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records
