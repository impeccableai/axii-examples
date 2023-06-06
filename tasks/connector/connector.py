import argparse


def read_from_file(filepath):
    l = list()
    with open(filepath) as f:
        for line in f:
            l.append(int(line))
    return l


def save_list(l, filepath):
    f = open(filepath, "w")
    for i in l:
        f.write(f"{i}\n")
    f.close()


def main(args):
    a = read_from_file(args.fib)
    b = read_from_file(args.gen)

    sums, diffs = list(), list()
    for i in range(min(len(a), len(b))):
        sums.append(a[i] + b[i])
        diffs.append(a[i] - b[i])

    save_list(sums, args.sum)
    save_list(diffs, args.diff)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fib", type=str, required=True)
    parser.add_argument("--gen", type=str, required=True)
    parser.add_argument("--sum", type=str, required=True)
    parser.add_argument("--diff", type=str, required=True)
    main(parser.parse_args())
