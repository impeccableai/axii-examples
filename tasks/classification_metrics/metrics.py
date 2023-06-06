import argparse
import pandas as pd
import csv


def main(args):
    df = pd.read_csv(args.dataset, sep=args.delimiter)

    header = ["MetricName", "MetricValue"]
    with open(args.metrics_csv, "w") as output_file:
        writer = csv.writer(output_file, delimiter=args.delimiter)
        writer.writerow(header)

        classes = df[args.y_column].unique()
        for cls in classes:
            cls_tp = df[(df[args.y_column] == cls) & (
                df[args.predicted_column] == cls)]
            cls_fp = df[(df[args.y_column] != cls) & (
                df[args.predicted_column] == cls)]
            cls_fn = df[(df[args.y_column] == cls) & (
                df[args.predicted_column] != cls)]
            cls_prec = len(cls_tp) / (len(cls_tp) + len(cls_fp))
            cls_recall = len(cls_tp) / (len(cls_tp) + len(cls_fn))
            cls_f1 = 2 / (1 / cls_prec + 1 / cls_recall)
            print(f"{cls}_Precision: {cls_prec}")
            writer.writerow([f"{cls}_Precision", cls_prec])
            print(f"{cls}_Recall: {cls_recall}")
            writer.writerow([f"{cls}_Recall", cls_recall])
            print(f"{cls}_F1: {cls_f1}")
            writer.writerow([f"{cls}_F1", cls_f1])

        accuracy = (df[args.y_column] ==
                    df[args.predicted_column]).sum() / len(df)

        print(f"Accuracy: {accuracy}")
        writer.writerow([f"Accuracy", accuracy])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Compute metrics for classification task")
    parser.add_argument("dataset", type=str, help="input CSV")
    parser.add_argument("metrics_csv", type=str, help="output CSV")
    parser.add_argument("-p", "--predicted_column", type=str,
                        required=True, help="predicted column")
    parser.add_argument("-y", "--y_column", type=str,
                        required=True, help="ground truth column")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    args = parser.parse_args()
    main(args)
