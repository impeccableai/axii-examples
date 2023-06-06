import argparse
import numpy as np
import pandas as pd

from joblib import load


def main(args):
    model = load(args.trained_model)
    print(model)
    predictions = model.predict(
        pd.read_csv(args.dataset, sep=args.delimiter))

    df = pd.DataFrame(predictions)
    df.columns = ["predicted"]
    df.to_csv(args.preds_csv, sep=args.delimiter, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Runs sklearn model on a CSV file and produces predictions CSV file")
    parser.add_argument("trained_model", type=str, help="trained model file")
    parser.add_argument("dataset", type=str, help="CSV data file")
    parser.add_argument("preds_csv", type=str,
                        help="CSV file with predictions")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    args = parser.parse_args()
    main(args)
