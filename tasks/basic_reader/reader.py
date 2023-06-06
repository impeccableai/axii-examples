import argparse


def main(args):
    acc = 0
    with open(args.input) as f:
        for line in f:
            acc += 1
    print(f"{acc}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    main(parser.parse_args())
