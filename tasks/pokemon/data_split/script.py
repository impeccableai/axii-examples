import argparse
import shutil
from distutils.dir_util import copy_tree


def main(args):

    copy_tree(f"{args.dataset}/images", args.images)
    shutil.copy(f"{args.dataset}/pokemon.csv", args.csv)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--images", type=str, required=True)
    parser.add_argument("--csv", type=str, required=True)
    main(parser.parse_args())
