import argparse
import os


def main(args):
    f = open(args.output, "w")
    for fileName in os.listdir(args.dir):
        f.write(f"{fileName}\n")
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
