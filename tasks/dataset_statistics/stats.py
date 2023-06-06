import argparse
import pandas as pd
import csv


def main(args):
    df = pd.read_csv(args.dataset, sep=args.delimiter)

    header = ["Name", "Value"]
    rows = []

    classes = df[args.y_column].unique()
    for cls in classes:
        rows += [(f"{cls}_count", len(df[df[args.y_column] == cls]))]

    feats = df.drop(args.y_column, axis=1)
    for column in feats.columns:
        rows += [(f"{column}_min", feats[column].min())]
        rows += [(f"{column}_max", feats[column].max())]
        rows += [(f"{column}_mean", feats[column].mean())]
        rows += [(f"{column}_median", feats[column].median())]

    with open(args.stats_csv, "w") as output_file:
        writer = csv.writer(output_file, delimiter=args.delimiter)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Compute dataset statistics")
    parser.add_argument("dataset", type=str, help="input CSV")
    parser.add_argument("stats_csv", type=str, help="output CSV")
    parser.add_argument("-y", "--y_column", type=str,
                        required=True, help="ground truth column")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    args = parser.parse_args()
    main(args)
