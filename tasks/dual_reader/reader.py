import argparse


def read_from_file(filepath):
    l = list()
    with open(filepath) as f:
        for line in f:
            l.append(int(line))
    return l


def main(args):
    a = read_from_file(args.a)
    b = read_from_file(args.b)

    for i in range(min(len(a), len(b))):
        print(a[i], b[i])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=str, required=True)
    parser.add_argument("--b", type=str, required=True)
    main(parser.parse_args())
