import argparse
import sys

import tensorflow as tf
import numpy as np


def main(args):
    if args.logdir:
        print(f"logging to: {args.logdir}")
        writer = tf.summary.create_file_writer(args.logdir)

        with writer.as_default():
            for step in range(100):
                tf.summary.scalar("sin(x)", np.sin(step), step=step)
    else:
        print(f"not logging")
    with open(args.model, "w") as f:
        f.write("so ML, much AI\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Tensorboard test")
    parser.add_argument("--model", type=str, help="model file")
    parser.add_argument("--logdir", type=str, help="train set file")
    args = parser.parse_args()
    sys.exit(main(args))
