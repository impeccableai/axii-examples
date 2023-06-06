import argparse
import pandas as pd


def main(args):
    print("Pandas version:", pd.__version__)
    print("Arguments:")
    print(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg", type=str, required=True)
    main(parser.parse_args())
