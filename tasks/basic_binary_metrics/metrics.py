import argparse
import pandas as pd
import csv


def main(args):
    df = pd.read_csv(args.dataset, sep=args.delimiter)
    df["cls"] = df[args.prob_column].round()
    df["correct"] = df[args.y_column] == df["cls"]

    df["tp"] = (df["cls"] == 1) & (df["correct"])
    df["fp"] = (df["cls"] == 1) & (~df["correct"])
    df["fn"] = (df["cls"] == 0) & (~df["correct"])

    acc = df["correct"].sum() / len(df)
    precision = df["tp"].sum() / (df["tp"].sum() + df["fp"].sum())
    recall = df["tp"].sum() / (df["tp"].sum() + df["fn"].sum())
    f1 = 2 / (1 / precision + 1 / recall)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1: {f1}")
    print(f"Accuracy: {acc}")

    header = ["Precision", "Recall", "F1", "Accuracy"]
    row = [precision, recall, f1, acc]

    with open(args.metrics_csv, "w") as output_file:
        writer = csv.writer(output_file, delimiter=args.delimiter)
        writer.writerow(header)
        writer.writerow(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Compute basic metrics for binary classification task")
    parser.add_argument("dataset", type=str, help="input CSV")
    parser.add_argument("metrics_csv", type=str, help="output CSV")
    parser.add_argument("-p", "--prob_column", type=str,
                        required=True, help="probability column")
    parser.add_argument("-y", "--y_column", type=str,
                        required=True, help="ground truth column")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    args = parser.parse_args()
    main(args)
