import argparse
import pandas as pd


def main(args):
    df = pd.read_csv(args.input)
    classes = {cls: id for id, cls in enumerate(df["Class"].unique())}
    df["Class"] = df["Class"].apply(lambda x: classes[x])
    df.to_csv(args.output, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "Preprocess Iris Dataset: replaces class names with encoded values")
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
