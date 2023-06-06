import argparse


def main(args):
    f = open(args.output, "w")
    for i in range(15):
        f.write(f"{i}\n")
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
