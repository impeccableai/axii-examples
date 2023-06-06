import argparse
import random


def main(args):
    if args.seed:
        random.seed(args.seed)

    with open(args.output, "w") as f:
        f.write(f'{random.randint(0, 100)}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Print args")
    parser.add_argument("--output", type=str, required=True, help="output")
    parser.add_argument("--seed", type=int, required=False, default=None)
    main(parser.parse_args())
