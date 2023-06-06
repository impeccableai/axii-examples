import argparse
import csv

_CABIN = "Cabin"


def main(args):
    read = 0
    write = 0
    header = True
    col_names = {}
    with open(args.input) as input_file:
        reader = csv.reader(input_file)
        with open(args.output, "w") as output_file:
            writer = csv.writer(output_file)
            for line in reader:
                read += 1
                if header:
                    header = False
                    col_names = {name: i for i, name in enumerate(line)}
                    line += ["CabinClass"]
                    writer.writerow(line)
                    continue
                line += [line[col_names[_CABIN]][0]
                         ] if len(line[col_names[_CABIN]]) > 0 else ["U"]
                writer.writerow(line)
                write += 1
    print(f"read {read} lines")
    print(f"wrote {write} lines")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="input csv")
    parser.add_argument("output", type=str, help="output csv")
    args = parser.parse_args()
    main(args)
