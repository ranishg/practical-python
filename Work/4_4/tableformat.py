# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print(f"{header:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f"{data:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="")
        for header in headers:
            print(f"<th>{header}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for data in rowdata:
            print(f"<td>{data}</td>", end="")
        print("</tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format {fmt}")


def print_table(objects, columns, formatter):
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)
