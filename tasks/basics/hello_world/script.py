import argparse


def main(args):
    print('Hello World')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args())
