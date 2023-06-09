import argparse
from pyspark.sql import SparkSession


def main(args):
    sc = SparkSession.builder.appName("PysparkExample").getOrCreate()

    sc.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
