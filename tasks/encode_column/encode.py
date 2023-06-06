import argparse
import csv


def main(args):
    header = args.has_header
    try:
        column_idx = int(args.column)
    except ValueError:
        column_idx = -1
    read = 0
    write = 0
    with open(args.input) as input_file:
        reader = csv.reader(input_file, delimiter=args.delimiter)
        with open(args.output, "w") as output_file:
            with open(args.encoded_column, "w") as output_column_file:
                writer = csv.writer(output_file, delimiter=args.delimiter)
                column_writer = csv.writer(output_column_file, delimiter=args.delimiter)
                col_values = {}
                for cols in reader:
                    read += 1
                    if header:
                        header = False
                        columns_idxs = {col: idx for idx, col in enumerate(cols)}
                        column_idx = columns_idxs[args.column]
                        writer.writerow(cols + [args.column + "_le"])
                        column_writer.writerow([args.column + "_le"])
                        write += 1
                        continue
                    if cols[column_idx] not in col_values:
                        col_values[cols[column_idx]] = len(col_values)
                    encoded = col_values[cols[column_idx]]
                    writer.writerow(cols + [encoded])
                    column_writer.writerow([encoded])
                    write += 1
    print(f"read {read} lines")
    print(f"wrote {write} lines")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Label encode column in a CSV fil")
    parser.add_argument("input", type=str, help="input file")
    parser.add_argument("output", type=str, help="output file")
    parser.add_argument("encoded_column", type=str, help="encoded column file")
    parser.add_argument("column", type=str,
                        help="column name or idx to encode")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    parser.add_argument("-hdr", "--has_header", type=bool, default=True,
                        help="whether the file has header (default: True")
    args = parser.parse_args()
    main(args)
