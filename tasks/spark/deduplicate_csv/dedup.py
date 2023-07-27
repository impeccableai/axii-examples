import argparse
import time
from pyspark.sql import SparkSession


def main(args):
    sc = SparkSession.builder.appName("PysparkExample").getOrCreate()

    dataframe = sc.read.option("header", "true").option(
        "mode", "DROPMALFORMED").csv(args.input)
    dataframe_dropdup = dataframe.dropDuplicates()
    dataframe_dropdup.coalesce(1).write.csv(args.output, mode="overwrite", header=True)
    sc.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
