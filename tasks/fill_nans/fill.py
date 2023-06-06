import argparse
import pandas as pd


def main(args):
    df = pd.read_csv(args.input_csv, sep=args.delimiter)
    if args.mode == "mean":
        val = df[~df[args.column].isna()][args.column].mean()
    elif args.mode == "min":
        val = df[~df[args.column].isna()][args.column].min()
    elif args.mode == "max":
        val = df[~df[args.column].isna()][args.column].max()
    elif args.mode == "const":
        val = args.value
    else:
        raise ValueError(f"Unknown mode: {args.mode}")

    print(f"Filling column `{args.column}` with: `{val}`")

    df.loc[df[args.column].isna(), args.column] = val
    df.to_csv(args.output_csv, sep=args.delimiter, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Fill NaNs in column")
    parser.add_argument("input_csv", type=str, help="input CSV")
    parser.add_argument("output_csv", type=str, help="output CSV")
    parser.add_argument("column", type=str, help="column to fill")
    parser.add_argument(
        "mode", choices=["mean", "max", "min", "const"], type=str, help="fill mode")
    parser.add_argument("--value", default=None, help="const value to fill")
    parser.add_argument("-d", "--delimiter", type=str,
                        default=",", help="column delimiter (default: ',')")
    args = parser.parse_args()
    main(args)
