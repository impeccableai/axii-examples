import argparse
import time
from pyspark.sql import SparkSession


def main(args):
    print("example.py > main starting")
    sc = SparkSession.builder.appName("PysparkExample").getOrCreate()

    print("example.py > main got session")
    dataframe = sc.read.option("header", "true").option(
        "mode", "DROPMALFORMED").csv(args.input)
    print("example.py > main read file, count:", dataframe.count())
    dataframe_dropdup = dataframe.dropDuplicates()
    print("example.py > main saving file, count:", dataframe_dropdup.count())
    dataframe_dropdup.coalesce(1).writemode('overwrite').option(
        "header", "true").csv(args.output)
    print("example.py > main stopping session")
    sc.stop()


if __name__ == "__main__":
    print("example.py starting")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
