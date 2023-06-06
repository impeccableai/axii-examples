import argparse
import csv


def select_columns(line, idxs):
    return [line[i] for i in range(len(line)) if i not in idxs], [line[i] for i in range(len(line)) if i in idxs]


def main(args):
    header = args.has_header
    column_idx = {}
    drop_columns = list(map(lambda x: x.strip(),
                            args.drop_columns.split(args.delimiter)))
    try:
        idxs_to_drop = set(map(int, drop_columns))
    except ValueError:
        idxs_to_drop = set()
    read = 0
    write = 0
    with open(args.input) as input_file:
        reader = csv.reader(input_file, delimiter=args.delimiter)
        with open(args.output, "w") as output_file:
            with open(args.dropped_columns, "w") as drop_cols_file:
                writer = csv.writer(output_file, delimiter=args.delimiter)
                drop_writer = csv.writer(
                    drop_cols_file, delimiter=args.delimiter)
                for line in reader:
                    read += 1
                    if header:
                        header = False
                        column_idx = {col: i for i, col in enumerate(line)}
                        if len(idxs_to_drop) == 0:
                            idxs_to_drop = set([column_idx[col]
                                                for col in drop_columns])
                        header_line, dropped_header = select_columns(
                            line, idxs_to_drop)
                        writer.writerow(header_line)
                        drop_writer.writerow(dropped_header)
                        write += 1
                        continue
                    cols, dropped = select_columns(line, idxs_to_drop)
                    writer.writerow(cols)
                    drop_writer.writerow(dropped)
                    write += 1
    print(f"read {read} lines")
    print(f"wrote {write} lines")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Drop columns from a file")
    parser.add_argument("--input", required=True, type=str, help="input file")
    parser.add_argument("--output", required=True,
                        type=str, help="output file")
    parser.add_argument("--dropped_columns", required=True,
                        type=str, help="dropped_columns file")
    parser.add_argument("--drop_columns", required=True, type=str,
                        help="comma separated list of column names or indices to drop")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    parser.add_argument("-hdr", "--has_header", type=bool, default=True,
                        help="whether the file has header (default: True")
    args = parser.parse_args()
    main(args)
