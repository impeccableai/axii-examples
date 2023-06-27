import argparse

def main(args):
    with open(args.file) as f:
        for line in f:
            print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, required=True)
    main(parser.parse_args())
