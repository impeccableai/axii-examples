import argparse


def main(args):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Python Template Task")
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("-p", "--parameter", type=bool, default=True,
                        help="parameter")
    main(parser.parse_args())
