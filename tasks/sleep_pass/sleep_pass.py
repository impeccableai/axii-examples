import argparse
import time


def main(args):
    time.sleep(args.time)
    with open(args.output, "w") as out_file:
        with open(args.input) as input_file:
            for line in input_file:
                out_file.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Sleep and pass-through")
    parser.add_argument("input", type=str, help="input file")
    parser.add_argument("output", type=str, help="output file")
    parser.add_argument("-t", "--time", default=60,
                        type=int, help="output file")
    args = parser.parse_args()
    main(args)
