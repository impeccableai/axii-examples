import argparse
import csv
import random


def main(args):
    random.seed(args.seed)
    header = args.has_header
    read = 0
    write = 0
    with open(args.input) as input_file:
        reader = csv.reader(input_file, delimiter=args.delimiter)
        with open(args.train_set, "w") as train_set_file:
            with open(args.test_set, "w") as test_set_file:
                train_writer = csv.writer(
                    train_set_file, delimiter=args.delimiter)
                test_writer = csv.writer(
                    test_set_file, delimiter=args.delimiter)
                for cols in reader:
                    read += 1
                    if header:
                        header = False
                        train_writer.writerow(cols)
                        test_writer.writerow(cols)
                        write += 1
                        continue
                    if random.random() < args.test_size:
                        test_writer.writerow(cols)
                    else:
                        train_writer.writerow(cols)
                    write += 1
    print(f"read {read} lines")
    print(f"wrote {write} lines")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Splits (randomly) a CSV file into train and test sets")
    parser.add_argument("input", type=str, help="input file")
    parser.add_argument("train_set", type=str, help="train set file")
    parser.add_argument("test_set", type=str, help="test set file")
    parser.add_argument("test_size", type=float, help="size of the test set")
    parser.add_argument("--seed", type=int, default=None, help="random seed")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    parser.add_argument("-hdr", "--has_header", type=bool, default=True,
                        help="whether the file has header (default: True")
    args = parser.parse_args()
    main(args)
